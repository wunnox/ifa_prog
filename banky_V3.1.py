##############################################
#
# Name: banky_V3.1.py
#
# Author: Peter Christen
#
# Version: 3.1
#
# Date: 20.02.2021
#
# Purpose: Kontoverwaltungsprogramm mit MySQL-Anbindung
#
##############################################

import datetime
import time
import os
import mysql.connector

# Variablen
kontobasis = 12345

# Mit Datenbank verbinden
connection = mysql.connector.connect(
    user='root',
    password='newpassword',
    host='localhost',
    database='banky')
cursor = connection.cursor()

# Datenbank Kommandos
insert_banky_kunden_statement = """insert into banky_kunden values(%s,%s,%s,%s,%s,%s,%s,%s)"""
insert_banky_konto_statement = """insert into banky_konto values(%s,%s,%s,%s,%s,%s)"""
insert_banky_transaktion = """insert into banky_transaktion values(%s,%s,%s,%s,%s)"""

select_banky_kunden_statement = """select * from banky_kunden where kunden_id=%s"""
select_banky_konto_statement = """select a.kontonr,c.kontotyp,a.kontostand,b.vorname,b.nachname,b.wohnort,a.erstellt,a.letzteaenderung from banky_konto a, banky_kunden b, banky_kontotyp c where a.kunden_id=b.kunden_id and a.kontotyp_id=c.kontotyp_id and a.kontonr = %s"""
select_banky_konto_liste_statement = """select a.kontonr,c.kontotyp,a.kontostand,b.vorname,b.nachname,b.wohnort,a.erstellt,a.letzteaenderung from banky_konto a, banky_kunden b, banky_kontotyp c where a.kunden_id=b.kunden_id and a.kontotyp_id=c.kontotyp_id"""
select_banky_maxkonto_statement = """select max(kontonr) from banky_konto"""
select_banky_kontostand = """select kontostand from banky_konto where kontonr = %s"""
select_banky_transaktion_5 = """select * from (select * from banky_transaktion where kontonr = %s order by trans_id desc limit 5)Var order by trans_id asc"""
select_banky_transaktion_all = """select * from banky_transaktion where kontonr = %s order by trans_id """

update_banky_kontostand = """update banky_konto set kontostand = %s, letzteaenderung = %s where kontonr = %s"""

# Funktionen


def kontonr_generieren():
    '''Neue Kontonummer definieren'''
    cursor.execute(select_banky_maxkonto_statement)
    for d in cursor:
        kto = d[0].split("-")
    kto[0] = int(kto[0]) + 1
    kontonr = str(kto[0]) + "-" + str(jahr)
    return kontonr


def test_daten_laden():
    '''Laden von Daten zum Testen'''
    print("Testdaten erfassen")
    #
    # Tabellen entleeren
    cursor.execute("delete from banky_kunden")
    cursor.execute("delete from banky_konto")
    cursor.execute("delete from banky_kontotyp")
    cursor.execute("delete from banky_transaktion")
    #
    # Neue Kontentyps erstellen
    insert_banky_kontotyp = """insert into banky_kontotyp values(%s,%s,%s)"""
    cursor.execute(
        insert_banky_kontotyp,
        (1,
         "Privatkonto",
         "Konto für natürliche Personen"))
    cursor.execute(insert_banky_kontotyp, (2, "Sparkonto",
                                           "Sparkonto für natürliche Personen"))
    cursor.execute(
        insert_banky_kontotyp,
        (3,
         "Kontokorrent",
         "Konto für juristische Personen"))
    #
    # Testkunden einfügen
    cursor.execute(
        insert_banky_kunden_statement,
        (1,
         'Herr',
         'Hans',
         'Muster',
         'Kramgasse 4',
         '3000 Bern',
         datum,
         datum))
    cursor.execute(
        insert_banky_kunden_statement,
        (2,
         'Frau',
         'Anna',
         'Meier',
         'Plantetenweg 8',
         '3110 Münsingen',
         datum,
         datum))
    cursor.execute(
        insert_banky_kunden_statement,
        (3,
         'Herr',
         'Remo',
         'Müller',
         'Finkenweg 20',
         '3006 Elfenau',
         datum,
         datum))
    cursor.execute(
        insert_banky_kunden_statement,
        (4,
         'Frau',
         'Irene',
         'Moser',
         'Scheuermat 12',
         '3013 Rubigen',
         datum,
         datum))
    #
    # Testkonten erstellen
    cursor.execute(insert_banky_konto_statement,
                   ('12345-21', 1200.00, 1, 1, datum, datum))
    cursor.execute(insert_banky_transaktion,
                   (0, '12345-21', 1200.00, 1200.00, datum))
    kontonr = kontonr_generieren()
    cursor.execute(insert_banky_konto_statement,
                   (kontonr, 3200.00, 2, 1, datum, datum))
    cursor.execute(insert_banky_transaktion,
                   (0, kontonr, 3200.00, 3200.00, datum))
    kontonr = kontonr_generieren()
    cursor.execute(insert_banky_konto_statement,
                   (kontonr, 221.00, 3, 1, datum, datum))
    cursor.execute(insert_banky_transaktion,
                   (0, kontonr, 221.00, 221.00, datum))
    kontonr = kontonr_generieren()
    cursor.execute(insert_banky_konto_statement,
                   (kontonr, 50.20, 4, 1, datum, datum))
    cursor.execute(insert_banky_transaktion, (0, kontonr, 50.20, 50.20, datum))
    #
    connection.commit()
    time.sleep(1)


def kunden_informationen_anzeigen(kunden_id):
    '''Kundeninformationen anzeigen'''

    cursor.execute(select_banky_kunden_statement, kunden_id)
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


def kunden_informationen():
    '''Kundeinformationen abfragen'''
    print("{0:<3}{1:<10}{2:<10}{3:<30}{4:<30}".format(
        "ID", "Nachname", "Vorname", "Adresse", "Wohnort"))
    cursor.execute("select * from banky_kunden order by Nachname")
    for d in cursor:
        print(
            "{0:<3}{1:<10}{2:<10}{3:<30}{4:<30}".format(
                d[0],
                d[3],
                d[2],
                d[4],
                d[5]))


def kunde_erfassen():
    '''Ein neuer Kunde erfassen'''

    anrede = input("Anrede: ")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    adresse = input("Adresse: ")
    wohnort = input("Wohnort: ")
    insert_banky_kunden_daten = (
        0,
        anrede,
        vorname,
        nachname,
        adresse,
        wohnort,
        datum,
        datum)
    cursor.execute(insert_banky_kunden_statement, insert_banky_kunden_daten)
    connection.commit()
    last_insert_id = cursor.lastrowid
    print()
    print("Folgender Kunde wurde erfasst:")
    print("===============================")
    print()
    kunden_informationen_anzeigen((last_insert_id,))


def konto_informationen_anzeigen(kontonr):
    cursor.execute(select_banky_konto_statement, kontonr)
    for d in cursor:
        print("Kontonummer   :", d[0])
        print("Kontotyp      :", d[1])
        print("Kontostand Fr.: %.2f" % d[2])
        print()
        print("Inhaber:")
        print("Vorname       :", d[3])
        print("Nachname      :", d[4])
        print("Wohnort       :", d[5])
        print("Erfasst       :", d[6])
        print("Letzte anp.   :", d[7])

    print()
    print("Letzte Transaktionen:")
    cursor.execute(select_banky_transaktion_5, kontonr)
    print("{0:>4}{1:^25}{2:>10}".format("ID", "Datum", "Betrag"))
    fm = '{0:>4}{1:>25}{2:>10.2f}'
    for d in cursor:
        print(fm.format(d[0], str(d[4]), d[2]))

    print()
    input("Weiter mit Return")


def konto_informationen():
    '''Kontoinformationen anzeigen'''
    konto_liste()
    print()
    while True:
        kontonr = input("Geben Sie die Kontonummer ein: ")
        if kontonr == "q":
            break
        else:
            print()
            print("Angaben zu Konto:", kontonr)
            print("==========================")
            konto_informationen_anzeigen((kontonr,))
            break


def konto_erfassen():
    kunden_informationen()
    print()
    kunden_id = input(
        "Für welchen Kunden wollen Sie ein Konto erfassen (Bitte ID eingeben): ")

    print("Verfügbare Konten:")
    print("==================")
    print()
    print("{0:<3}{1:<20}{2:<40}".format("ID", "Typ", "Beschreibung"))
    cursor.execute("select * from banky_kontotyp")
    for d in cursor:
        print("{0:<3}{1:<20}{2:<40}".format(d[0], d[1], d[2]))

    print()
    kontotyp_id = input(
        "Welcher Kontentyp wollen Sie erfassen (Bitte ID eingeben): ")
    print()

    kontonr = kontonr_generieren()
    insert_banky_konto_daten = (
        kontonr,
        0,
        int(kunden_id),
        int(kontotyp_id),
        datum,
        datum)
    cursor.execute(insert_banky_konto_statement, insert_banky_konto_daten)
    connection.commit()
    return kontonr


def konto_liste():
    '''Vorhandene Konten auflisten'''
    print(
        "{0:<15}{1:<15}{2:^13}{3:<10}{4:<15}{5:<15}".format(
            "Kontonummer",
            "Kontotyp",
            "Stand",
            "Vorname",
            "Nachname",
            "Wohnort"))

    cursor.execute(select_banky_konto_liste_statement)
    for d in cursor:
        print("{0:<15}{1:<15}{2:>8.2f}{3:>4}{4:<10}{5:<15}{6:<15}".format(
            d[0], d[1], d[2], " Fr. ", d[3], d[4], d[5]))


def konto_transaktion(kontonr, betrag, operation):
    '''Konto Transaktionen durchführen'''

    # Aktueller Kontostand aus DB einlesen
    cursor.execute(select_banky_kontostand, (kontonr,))
    for d in cursor:
        kontostand = d[0]

    # Neuer Kontostand errechnen
    if operation == "+":
        betrag = float(betrag)
    else:
        betrag = float(betrag) * -1
    neuerkontostand = kontostand + betrag

    # Neuer Kontostand in DB schreiben
    cursor.execute(update_banky_kontostand, (neuerkontostand, datum, kontonr))
    # Transaktion in DB schreiben
    cursor.execute(
        insert_banky_transaktion,
        (0,
         kontonr,
         betrag,
         neuerkontostand,
         datum))
    connection.commit()

    return neuerkontostand


def konto_einzahlen():
    '''Betrag auf Konto einzalhlen'''

    print("Geld auf Konto einzahlen")
    print("========================")
    print()
    konto_liste()

    print()
    kontonr = input(
        "Auf welches Konto wollen Sie einzahlen (Bitte Kontonummer angeben): ")
    betrag = float(input("Bitte einzuzahlender Betrag eingeben: "))

    aktuellerkontostand = konto_transaktion(kontonr, betrag, "+")

    print("Konto                   :", kontonr)
    print("Einbezahlt           Fr.: %.2f" % betrag)
    print("Aktueller Kontostand Fr.: %.2f" % aktuellerkontostand)
    print()
    input("Weiter mit Return")


def konto_auszahlen():
    '''Betrag von Konto beziehen'''

    print("Geld von Konto beziehen")
    print("========================")
    print()
    konto_liste()

    print()
    kontonr = input(
        "Von welchem Konto wollen Sie Geld beziehen (Bitte Kontonummer angeben): ")
    betrag = float(input("Bitte auszuzahlender Betrag eingeben: "))

    aktuellerkontostand = konto_transaktion(kontonr, betrag, "-")

    print("Konto                   :", kontonr)
    print("Bezogen              Fr.: %.2f" % betrag)
    print("Aktueller Kontostand Fr.: %.2f" % aktuellerkontostand)
    print()
    input("Weiter mit Return")


def konto_transaktionen_anzeigen():
    '''Konto Transaktionen anzeigen'''

    print("Transaktionen anzeigen")
    print("========================")
    print()
    konto_liste()
    konto_liste()
    print()

    while True:
        kontonr = input("Geben Sie die Kontonummer ein: ")
        if kontonr == "q":
            break
        else:
            print()
            print("Transaktionen für Konto:", kontonr)
            cursor.execute(select_banky_transaktion_all, (kontonr,))
            print(
                "{0:>4}{1:^25}{2:^10}{3:>10}".format(
                    "ID",
                    "Datum",
                    "Betrag",
                    "Kontostand"))
            fm = '{0:>4}{1:>25}{2:>10.2f}{3:>10.2f}'
            for d in cursor:
                print(fm.format(d[0], str(d[4]), d[2], d[3]))
            break


# Main block
wahl = 0
konto = {}
validchoise = ("1", "2", "3", "4", "5", "6", "7", "8", "q", "x")
while wahl != 'q':
    os.system("clear")
    print("Applikation Banky")
    print("=================")
    print("1. Kunde erfassen")
    print("2. Kundeninformationen anzeigen")
    print("3. Konto erfassen")
    print("4. Kontoinformationen anzeigen")
    print("5. Kontenliste anzeigen")
    print("6. Geld auf Konto einzahlen")
    print("7. Geld von Konto beziehen")
    print("8. Transaktionen anzeigen")
    print("q  Ende")
    print()
    wahl = input("Ihre Wahl: ")

    # Aktuelles Datum und Zeit setzen
    now = datetime.datetime.now()
    jahr = now.strftime("%y")
    datum = now.strftime("%Y-%m-%d %H:%M:%S")

    if wahl not in validchoise:
        print(wahl, "ist eine ungültige Wahl")
        time.sleep(2)
    elif wahl == "1":
        print()
        print("Neuer Kunde erfassen:")
        print("=====================")
        print()
        kunde_erfassen()
    elif wahl == "2":
        print("Kundeninformationen anzeigen")
        print("=============================")
        print()
        kunden_informationen()
        kunden_id = input(
            "Für welchen Kunden wollen Sie die Informationen sehen (Bitte ID eingeben): ")
        print()
        print("Kundeninformationen")
        print("===================")
        print()
        kunden_informationen_anzeigen((kunden_id,))
    elif wahl == "3":
        print()
        print("Kontoerfassen")
        print("=============")
        print()
        kontonr = konto_erfassen()
        print("Folgendes Konto wurde erfasst:")
        print("==============================")
        print()
        konto_informationen_anzeigen((kontonr,))
    elif wahl == "4":
        print("Kontoinformationen anzeigen")
        print("===========================")
        print()
        konto_informationen()
    elif wahl == "5":
        print()
        print("Vorhandene Kontonummern:")
        print("========================")
        print()
        konto_liste()
        input("Weiter mit Return")
    elif wahl == "6":
        konto_einzahlen()
    elif wahl == "7":
        konto_auszahlen()
    elif wahl == "8":
        konto_transaktionen_anzeigen()
        print()
        input("Weiter mit Return")
    elif wahl == "x":
        test_daten_laden()
