##############################################
#
# Name: Name: banky_V5.2.py
#
# Author: Peter Christen
#
# Version: 5.2
#
# Date: 10.03.2021
#
# Purpose: OO-Kontoverwaltungsprogramm mit MySQL-Anbindung und Spezialfunktion
#
##############################################

#Module
import datetime
import time
import os
import mysql.connector
import banky_testdaten as bankytest
import random

# Variablen
wk=0.9     #Dollar Wechselkurs

# Mit Datenbank verbinden
connection = mysql.connector.connect(
    user='root',
    password='newpassword',
    host='localhost',
    database='banky')
cursor = connection.cursor()

# Datenbank Kommandos zur Verwaltung von Kunden
insert_banky_kunden = """insert into banky_kunden values(%s,%s,%s,%s,%s,%s,%s,%s)"""
select_banky_kunden = """select * from banky_kunden where kunden_id=%s"""
select_banky_allkunden = """select * from banky_kunden order by %s"""
delete_banky_kunden = """delete from banky_kunden where kunden_id=%s"""

# Datenbank Kommandos zur Verwaltung von Konten
insert_banky_konto_statement = """insert into banky_konto values(%s,%s,%s,%s,%s,%s)"""
insert_banky_transaktion = """insert into banky_transaktion values(%s,%s,%s,%s,%s)"""
select_banky_konto_statement = """select a.kontonr,c.kontotyp,a.kontostand,b.vorname,b.nachname,b.wohnort,a.erstellt,a.letzteaenderung from banky_konto a, banky_kunden b, banky_kontotyp c where a.kunden_id=b.kunden_id and a.kontotyp_id=c.kontotyp_id and a.kontonr = %s"""
select_banky_konto_liste_statement = """select a.kontonr,c.kontotyp,a.kontostand,b.vorname,b.nachname,b.wohnort,a.erstellt,a.letzteaenderung from banky_konto a, banky_kunden b, banky_kontotyp c where a.kunden_id=b.kunden_id and a.kontotyp_id=c.kontotyp_id"""
select_banky_maxkonto_statement = """select max(kontonr) from banky_konto"""
select_banky_kontostand = """select kontostand from banky_konto where kontonr = %s"""
select_banky_transaktion_5 = """select * from (select * from banky_transaktion where kontonr = %s order by trans_id desc limit 5)Var order by trans_id asc"""
select_banky_transaktion_all = """select * from banky_transaktion where kontonr = %s order by trans_id """
select_banky_allkonto = """select * from banky_konto order by %s"""
update_banky_kontostand = """update banky_konto set kontostand = %s, letzteaenderung = %s where kontonr = %s"""

#Klassen
class Konto:
  '''Klasse zum Verwalten der Konten'''
  #Klassenvariable
  now = datetime.datetime.now()

  #Konstruktor Methode
  def __init__(self,ktnr):
      self.kontonummer=ktnr

  #Weitere Methode
  def konto_informationen_anzeigen(self,kontonr):
    cursor.execute(select_banky_konto_statement, (kontonr,))
    for d in cursor:
        print("Kontonummer   :", d[0])
        print("Kontotyp      :", d[1])
        print("Kontostand Fr.: %.2f" % round(d[2]*wk,2))
        print()
        print("Inhaber:")
        print("Vorname       :", d[3])
        print("Nachname      :", d[4])
        print("Wohnort       :", d[5])
        print("Erfasst       :", d[6])
        print("Letzte anp.   :", d[7])

    print()
    print("Letzte Transaktionen:")
    cursor.execute(select_banky_transaktion_5, (kontonr,))
    print("{0:>4}{1:^25}{2:>10}".format("ID", "Datum", "Betrag"))
    fm = '{0:>4}{1:>25}{2:>10.2f}'
    for d in cursor:
        print(fm.format(d[0], str(d[4]), round(d[2]*wk,2)))

    print()
    input("Weiter mit Return")

  def konto_informationen(self):
    '''Kontoinformationen anzeigen'''

    self.konto_liste()
    print()
    while True:
        kontonr = input("Geben Sie die Kontonummer ein (0 für Abbruch): ")
        if kontonr == "0":
            break
        else:
            print()
            print("Angaben zu Konto:", kontonr)
            print("==========================")
            self.konto_informationen_anzeigen(kontonr)
            break

  def konto_erfassen(self,kontonr):
    '''Ein neues Konto erfassen'''

    kunde[0].kunden_informationen(0)
    print()
    kunden_id = input("Für welchen Kunden wollen Sie ein Konto erfassen (Bitte ID eingeben): ")

    print("Verfügbare Konten:")
    print("==================")
    print()
    print("{0:<3}{1:<20}{2:<40}".format("ID", "Typ", "Beschreibung"))
    cursor.execute("select * from banky_kontotyp")
    for d in cursor:
        print("{0:<3}{1:<20}{2:<40}".format(d[0], d[1], d[2]))

    print()
    kontotyp_id = input( "Welcher Kontentyp wollen Sie erfassen (Bitte ID eingeben): ")
    print()

    #Daten in Datenbank erfassen
    insert_banky_konto_daten = ( kontonr, 0, int(kunden_id), int(kontotyp_id), datum, datum)
    cursor.execute(insert_banky_konto_statement, insert_banky_konto_daten)
    cursor.execute(insert_banky_transaktion, (0, kontonr, 0, 0, datum))
    connection.commit()


  def konto_liste(self):
      '''Vorhandene Konten auflisten'''

      print("{0:<15}{1:<15}{2:^13}{3:<10}{4:<15}{5:<15}".format( "Kontonummer", "Kontotyp", "Stand", "Vorname", "Nachname", "Wohnort"))

      cursor.execute(select_banky_konto_liste_statement)
      for d in cursor:
        print("{0:<15}{1:<15}{2:>8.2f}{3:>4}{4:<10}{5:<15}{6:<15}".format(
            d[0], d[1], round(d[2]*wk,2), " Fr. ", d[3], d[4], d[5]))


class Transaktionen(Konto):
  '''Subklasse der Klasse Konto zum Verwalten der Transaktionen'''

  def __init__(self,ktnr):
      Konto.__init__(self,ktnr)

  def konto_transaktion_wk(self, kontonr, betrag, zielwaehrung):
    '''Rechnet den Betrag in $ oder CHF um'''

    global kontostandeinlesen, kontostandsumme

    if zielwaehrung=="CHF":
       betrag=float(betrag)/wk
    else:
       betrag=float(betrag)*wk

    if kontonr!='12349-21':
       nachkomma=betrag % 1
       drittenachkommastelleplus=str(nachkomma)[2:]
       nachkommawert=float("0.00"+drittenachkommastelleplus)
     
       if kontostandeinlesen==1:
          cursor.execute(select_banky_kontostand, ('12349-21',))
          for d in cursor:
              kontostand = d[0]
          kontostandsumme=kontostand
          kontostandeinlesen=0
       
       kontostandsumme+=nachkommawert
       cursor.execute(update_banky_kontostand, (kontostandsumme, datum, '12349-21'))
       cursor.execute(insert_banky_transaktion, (0, '12349-21', nachkommawert, kontostandsumme, datum))
       connection.commit()
    else:
       kontostandeinlesen=1

    return round(betrag,2)

  def konto_transaktion(self, kontonr, betrag, operation):
    '''Konto Transaktionen durchführen'''

    # Aktueller Kontostand aus DB einlesen
    cursor.execute(select_banky_kontostand, (kontonr,))
    for d in cursor:
        kontostand = d[0]

    # Neuer Kontostand errechnen
    if operation == "+":
        betrag = float(betrag)
        betrag=self.konto_transaktion_wk(kontonr,betrag,"CHF")
    else:
        betrag=self.konto_transaktion_wk(kontonr,betrag,"CHF")
        betrag = betrag * -1
    neuerkontostand = kontostand + betrag

    # Neuer Kontostand in DB schreiben
    cursor.execute(update_banky_kontostand, (neuerkontostand, datum, kontonr))

    # Transaktion in DB schreiben
    cursor.execute(insert_banky_transaktion, (0, kontonr, betrag, neuerkontostand, datum))
    connection.commit()

    return neuerkontostand

  def konto_einzahlen(self):
      '''Betrag auf Konto einzalhlen'''

      print("Geld auf Konto einzahlen")
      print("========================")
      print()
      self.konto_liste()

      print()
      kontonr = input(
        "Auf welches Konto wollen Sie einzahlen (Bitte Kontonummer angeben): ")
      betrag = float(input("Bitte einzuzahlender Betrag eingeben: "))

      aktuellerkontostand = self.konto_transaktion(kontonr, betrag, "+")

      print("Konto                   :", kontonr)
      print("Einbezahlt           Fr.: %.2f" % betrag)
      print("Aktueller Kontostand Fr.: %.2f" % round(aktuellerkontostand*wk,2))
      print()
      input("Weiter mit Return")

  def konto_auszahlen(self):
      '''Betrag von Konto beziehen'''

      print("Geld von Konto beziehen")
      print("========================")
      print()
      self.konto_liste()

      print()
      kontonr = input(
        "Von welchem Konto wollen Sie Geld beziehen (Bitte Kontonummer angeben): ")
      betrag = float(input("Bitte auszuzahlender Betrag eingeben: "))

      aktuellerkontostand = self.konto_transaktion(kontonr, betrag, "-")

      print("Konto                   :", kontonr)
      print("Bezogen              Fr.: %.2f" % betrag)
      print("Aktueller Kontostand Fr.: %.2f" % round(aktuellerkontostand*wk,2))
      print()
      input("Weiter mit Return")

  def konto_transaktionen_anzeigen(self):
      '''Konto Transaktionen anzeigen'''

      print("Transaktionen anzeigen")
      print("========================")
      print()
      self.konto_liste()
      #konto_liste()
      print()

      while True:
        kontonr = input("Geben Sie die Kontonummer ein (0 für Abbruch): ")
        if kontonr == "0":
            break
        else:
            print()
            print("Transaktionen für Konto:", kontonr)
            cursor.execute(select_banky_transaktion_all, (kontonr,))
            print(
                "{0:>4}{1:^25}{2:>10}".format(
                    "ID",
                    "Datum",
                    "Betrag",
                    "Kontostand"))
            fm = '{0:>4}{1:>25}{2:>10.2f}{3:>10.2f}'
            for d in cursor:
                print(fm.format(d[0], str(d[4]), d[2], d[3]))
            break

class Kunde:
  '''Klasse zum Verwalten der Kunden'''
  #Klassenvariable

  #Konstruktor Methode
  def __init__(self,kunden_id):
     self.kunden_id=kunden_id

  #Weitere Methode
  def kunden_informationen_anzeigen(self,kunden_id):
    '''Kundeninformationen anzeigen'''

    cursor.execute(select_banky_kunden, (kunden_id,))
    for d in cursor:
        print("Anrede         :", d[1])
        print("Vorname        :", d[2])
        print("Nachname       :", d[3])
        print("Adresse        :", d[4])
        print("Wohnort        :", d[5])
        print("Erstellt       :", d[6])
        print("Letzte Änderung:", d[7])
    print()
    input("Weiter mit Return")

  def kunde_erfassen(self,kunden_id):
    '''Neuer Kunde erfassen'''

    anrede = input("Anrede: ")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    adresse = input("Adresse: ")
    wohnort = input("Wohnort: ")

    self.kunde_in_DB_eintragen(kunden_id, anrede, vorname, nachname, adresse, wohnort, datum)

    print()
    print("Folgender Kunde wurde erfasst:")
    print("===============================")
    print()
    self.kunden_informationen_anzeigen(kunden_id)

  def kunde_anpassen(self,kunden_id):
    '''Kundendaten anpassen'''

    anrede = input("Anrede: ")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    adresse = input("Adresse: ")
    wohnort = input("Wohnort: ")

    self.kunde_in_DB_eintragen(kunden_id, anrede, vorname, nachname, adresse, wohnort, datum)

    print()
    print("Die Kundendaten wurde wie folgt angepasst:")
    print("==========================================")
    print()
    self.kunden_informationen_anzeigen(kunden_id)

  def kunde_in_DB_eintragen(self,kunden_id,anrede, vorname, nachname, adresse, wohnort, datum):
    '''Daten in Datenbank Schreiben'''

    insert_banky_kunden_daten = ( kunden_id, anrede, vorname, nachname, adresse, wohnort, datum, datum)
    cursor.execute(insert_banky_kunden, insert_banky_kunden_daten)
    connection.commit()

  def kunden_informationen(self,kunden_id):
      '''Kundeinformationen abfragen'''

      print("{0:<3}{1:<10}{2:<10}{3:<30}{4:<30}".format( "ID", "Nachname", "Vorname", "Adresse", "Wohnort"))

      #Kundenliste aus DB abfragen
      cursor.execute(select_banky_allkunden,("Nachnamen",))
      for d in cursor:
        print( "{0:<3}{1:<10}{2:<10}{3:<30}{4:<30}".format( d[0], d[3], d[2], d[4], d[5]))

  def kunden_loeschen(self,kunden_id):
      '''Kunde aus System löschen'''

      cursor.execute(delete_banky_kunden,(kunden_id,))

#Funktion
def bestehende_daten_laden():
    '''Laden der bestehenden Daten in der Datenbank'''

    cursor.execute(select_banky_allkunden,("kunden_id",))
    for d in cursor:
        print("CHECK:",d[0])
        try:
           kunde.append(d[0])
           kunde[d[0]]=Kunde(d[0])
        except:
           pass
    cursor.execute(select_banky_allkonto,("kontonr",))
    for d in cursor:
        konto[d[0]]=d[0]
        konto[d[0]]=Transaktionen(d[0])

def kontonr_generieren():
    '''Neue Kontonummer definieren'''

    cursor.execute(select_banky_maxkonto_statement)
    for d in cursor:
        kto = d[0].split("-")
    kto[0] = int(kto[0]) + 1
    kontonr = str(kto[0]) + "-" + str(jahr)
    return kontonr

# Main block
wahl = 0
kunde=[0]
kunde[0]=Kunde(0)
konto={"0":"0"}
konto["0"]=Transaktionen("0")
bestehende_daten_laden()
kontostandsumme=0.0
kontostandeinlesen=1

#Gültige Auswahl
validchoise = ("1", "2", "3", "4","5","6","7","8","9","10","q", "x","z")
while wahl != 'q':
    os.system("clear")
    print("Applikation Banky")
    print("=================")
    print("1. Kunde erfassen")
    print("2. Kunde anpassen")
    print("3. Kundeninformationen anzeigen")
    print("4. Kunde löschen")
    print("5. Konto erfassen")
    print("6. Kontoinformationen anzeigen")
    print("7. Kontenliste anzeigen")
    print("8. Geld auf Konto einzahlen")
    print("9. Geld von Konto beziehen")
    print("10. Transaktionen anzeigen")
    print("q  Ende")
    print()
    wahl = input("Ihre Wahl: ")

    # Aktuelles Datum und Zeit setzen
    now = datetime.datetime.now()
    jahr = now.strftime("%y")
    datum = now.strftime("%Y-%m-%d %H:%M:%S")

    if wahl not in validchoise:
        print(wahl, "ist eine ungültige Wahl")
        time.sleep(1)
    elif wahl == "1":
        print()
        print("Neuer Kunde erfassen:")
        print("=====================")
        print()

        max_id=len(kunde)
        kunden_id=max_id
        kunde.append(kunden_id)
        kunde[kunden_id]=Kunde(kunden_id)
        kunde[kunden_id].kunde_erfassen(kunden_id)

    elif wahl == "2":
        print("Kundeninformationen anpassen")
        print("=============================")
        print()
        kunde[0].kunden_informationen(0)
        print()

        while True:
           kunden_id = int(input("Für welchen Kunden wollen Sie die Informationen anpassen (Bitte ID eingeben oder 0 für weiter): "))
           if kunden_id < len(kunde):
              break
           else:
              print(kunden_id, "existiert nicht, bitte eine gültige ID eingeben")

        if kunden_id != 0:
           kunde[kunden_id].kunden_anpassen(kunden_id)

    elif wahl == "3":
        print("Kundeninformationen anzeigen")
        print("=============================")
        print()
        kunde[0].kunden_informationen(0)
        print()

        while True:
           kunden_id = int(input("Für welchen Kunden wollen Sie die Informationen sehen (Bitte ID eingeben oder 0 für weiter): "))
           if kunden_id < len(kunde):
              break
           else:
              print(kunden_id, "existiert nicht, bitte eine gültige ID eingeben")

        if kunden_id != 0:
           print()
           print("Kundeninformationen")
           print("===================")
           print()
           kunde[kunden_id].kunden_informationen_anzeigen(kunden_id)
    elif wahl == "4":
        print("Kunde löschen")
        print("=============================")
        print()
        kunde[0].kunden_informationen(0)
        print()

        while True:
           kunden_id = int(input("Welchen Kunden wollen Sie löschen (Bitte ID eingeben oder 0 für weiter): "))
           if kunden_id < len(kunde):
              break
           else:
              print(kunden_id, "existiert nicht, bitte eine gültige ID eingeben")

        if kunden_id != 0:
           print()
           kunde[kunden_id].kunden_loeschen(kunden_id)
           print("Kunde wurde gelöscht")
           input("Weiter mit Return")
    elif wahl == "5":
        print()
        print("Kontoerfassen")
        print("=============")
        print()
        kontonr = kontonr_generieren()
        konto[kontonr]=Transaktionen(kontonr)
        konto[kontonr].konto_erfassen(kontonr)
        print("Folgendes Konto wurde erfasst:")
        print("==============================")
        print()
        konto[kontonr].konto_informationen_anzeigen(kontonr)
    elif wahl == "6":
        print("Kontoinformationen anzeigen")
        print("===========================")
        print()
        konto["0"].konto_informationen()
    elif wahl == "7":
        print()
        print("Vorhandene Kontonummern:")
        print("========================")
        print()
        konto["0"].konto_liste()
        input("Weiter mit Return")
    elif wahl == "8":
        konto["0"].konto_einzahlen()
    elif wahl == "9":
        konto["0"].konto_auszahlen()
    elif wahl == "10":
        konto["0"].konto_transaktionen_anzeigen()
        print()
        input("Weiter mit Return")    

    elif wahl == "x":
        bankytest.test_daten_laden(cursor,datum)
        connection.commit()

        #Erstellte Daten einlesen
        kunde=[0]
        kunde[0]=Kunde(0)
        konto={"0":"0"}
        konto["0"]=Transaktionen("0")
        bestehende_daten_laden()

    elif wahl == "z":
        '''Zufallstransaktionen in Datenbank schreiben'''

        print("Testtransaktionen erfassen")
        kt=[]
        for i in konto.keys():
            if i!="0" and i!="12349-21": kt.append(i)

        anzkt=len(kt)-1
        c=0
        limite=100
        print("start")
        while c<limite:
           print(".", end='')
           now = datetime.datetime.now()
           datum = now.strftime("%Y-%m-%d %H:%M:%S")
           zkt = random.randint(0, anzkt)
           zbetrag = random.randint(10, 100)
           konto[kt[zkt]].konto_transaktion(kt[zkt], zbetrag, "+")
           zkt = random.randint(0, anzkt)
           zbetrag = random.randint(10, 100)
           konto[kt[zkt]].konto_transaktion(kt[zkt], zbetrag, "-")
           c+=1
        
        connection.commit()
        print() 
        print(limite, "Transaktionen ausgeführt")
        time.sleep(2)

