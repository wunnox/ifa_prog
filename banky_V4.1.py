##############################################
#
# Name: Name: banky_V4.1.py
#
# Author: Peter Christen
#
# Version: 4.1
#
# Date: 20.02.2021
#
# Purpose: OO-Kontoverwaltungsprogramm mit MySQL-Anbindung
#
##############################################

import datetime
import time
import os
import mysql.connector
import banky_testdaten as bankytest

# Variablen

# Mit Datenbank verbinden
connection = mysql.connector.connect(
    user='root',
    password='newpassword',
    host='localhost',
    database='banky')
cursor = connection.cursor()

# Datenbank Kommandos
insert_banky_kunden = """insert into banky_kunden values(%s,%s,%s,%s,%s,%s,%s,%s)"""
select_banky_kunden = """select * from banky_kunden where kunden_id=%s"""
select_banky_allkunden = """select * from banky_kunden order by %s"""
delete_banky_kunden = """delete from banky_kunden where kunden_id=%s"""

#Klassendefinitionen
class Kunde:
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


#Funktionen
def bestehende_daten_laden():
    '''Laden der bestehenden Daten in der Datenbank'''

    cursor.execute(select_banky_allkunden,("kunden_id",))
    for d in cursor:
        try:
           kunde.append(d[0])
           kunde[d[0]]=Kunde(d[0])
        except:
           pass


# Main block
wahl = 0
kunde=[0]
kunde[0]=Kunde(0)
bestehende_daten_laden()

#Gültige Auswahl definieren
validchoise = ("1", "2", "3", "4", "q", "x")
while wahl != 'q':
    os.system("clear")
    print("Applikation Banky")
    print("=================")
    print("1. Kunde erfassen")
    print("2. Kunde anpassen")
    print("3. Kundeninformationen anzeigen")
    print("4. Kunde löschen")
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

    elif wahl == "x":
        bankytest.test_daten_laden(cursor,datum)
        connection.commit()
