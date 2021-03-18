##############################################
#
# Name: banky_V2.py
#
# Author: Peter Christen
#
# Version: 2.0
#
# Date: 20.02.2021
#
# Purpose: Kontoverwaltungsprogramm mit Funktionen
#
##############################################

import datetime
import time
import os

# Variablen
kontobasis = 12345
kundennr = 0
wahl = 0
konto = {}
kunde = {}

# Funktionen


def kontonr_generieren():
    '''Neue Kontonummer generieren'''
    global kontobasis
    kontobasis += 1
    kontonr = str(kontobasis) + "-" + str(jahr)
    return kontonr


def test_daten_laden():
    '''Laden von Daten zum Testen'''
    global kontobasis, kundennr
    print("Testdaten erfassen")
    kundennr += 1
    kunde[kundennr] = (
        "Max",
        "Muster",
        "Stauffacherstrasse 20",
        "3000 Bern",
        datum)
    kundennr += 1
    kunde[kundennr] = (
        "Anna",
        "Studer",
        "Finkenweg 26",
        "3110 Münsingen",
        datum)
    kundennr += 1
    kunde[kundennr] = (
        "Fred",
        "Erb",
        "Laupenstrasse 3",
        "3000 Bern",
        datum)

    kontonr = kontonr_generieren()
    konto[kontonr] = [
        "privat",
        100.00,
        "Max",
        "Muster",
        "3000 Bern",
        datum]

    kontonr = kontonr_generieren()
    konto[kontonr] = [
        "privat",
        1200.20,
        "Anna",
        "Studer",
        "3110 Münsingen",
        datum]

    kontonr = kontonr_generieren()
    konto[kontonr] = ["privat", 50.00, "Fred", "Erb", "3000 Bern", datum]
    time.sleep(1)


def kunde_erfassen():
    '''Erfassen eines neuen Kunden'''
    global kundennr
    print("Neuer Kunde erfassen")
    print("====================")
    kundennr += 1
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    adresse = input("Adresse: ")
    wohnort = input("Wohnort: ")
    kunde[kundennr] = (vorname, nachname, adresse, wohnort, datum)
    print()
    print("Folgender Kunde wurde erfasst:")
    print("==============================")
    print()
    print("Kundennr:", kundennr)
    print("Vorname:", vorname)
    print("Nachname:", nachname)
    print("Adresse:", adresse)
    print("Wohnort:", wohnort)
    print("Erstellt:", datum)
    print()
    input("Weiter mit Return")


def kunden_informationen():
    print("{0:<5}{1:<15}{2:<20}{3:<20}".format(
        "ID", "Vorname", "Nachname", "Wohnort"))
    for k in kunde.keys():
        print("{0:<5}{1:<15}{2:<20}{3:<20}".format(
            k, kunde[k][0], kunde[k][1], kunde[k][3]))


def konto_daten_anzeigen(kontonr):
    print()
    print("Kontonummer:", kontonr)
    print("Kontotyp   :", konto[kontonr][0])
    print("Vorname    :", konto[kontonr][1])
    print("Nachname   :", konto[kontonr][2])
    print("Wohnort    :", konto[kontonr][3])
    print("Erfasst am :", konto[kontonr][4])
    print()
    input("Weiter mit Return")


def konto_erfassen():
    '''Ein neues Kontoerfassen'''
    global kontobasis

    print("Neues Konto erfassen")
    print("====================")

    kunden_informationen()
    print()
    id = int(
        input("Für welchen Kunden wollen Sie ein Konto erstellen (bitte ID angeben): "))

    kontonr = kontonr_generieren()
    konto[kontonr] = [
        "privat",
        0,
        kunde[id][0],
        kunde[id][1],
        kunde[id][2],
        datum]
    print()
    print("Folgendes Konto wurde erfasst:")
    print("Kontonummer:", kontonr)
    print("Kontotyp   :", konto[kontonr][0])
    print("Kontostand :", konto[kontonr][1])
    print("Vorname    :", konto[kontonr][2])
    print("Nachname   :", konto[kontonr][3])
    print("Wohnort    :", konto[kontonr][4])
    print("Erfasst am :", konto[kontonr][5])
    print()
    input("Weiter mit Return")


def konto_informationen():
    '''Kontoinformationen anzeigen'''
    print("Kontoinformationen anzeigen")
    print("===========================")
    print()
    konto_liste()
    print()

    while True:
        kontonr = input(
            "Für welche Kontonummer wollen Sie die Angaben sehen: ")
        if kontonr == "q":
            break
        elif kontonr not in konto.keys():
            print(kontonr, "ist keine bekannte Kontonummer")
        else:
            print()
            print("Angaben zu Konto:", kontonr)
            print("Kontotyp   :", konto[kontonr][0])
            print("Kontostand : %.2f" % konto[kontonr][1])
            print("Vorname    :", konto[kontonr][2])
            print("Nachname   :", konto[kontonr][3])
            print("Wohnort    :", konto[kontonr][4])
            print("Erfasst am :", konto[kontonr][5])
            print()
            input("Weiter mit Return")
            break


def konto_liste():
    print(
        "{0:<10}{1:<15}{2:<20}{3:<20}".format(
            "Konto",
            "Vorname",
            "Nachname",
            "Wohnort",
            "Erstellt"))
    for k in konto.keys():
        print(
            "{0:<10}{1:<15}{2:<20}{3:<20}".format(
                k,
                konto[k][2],
                konto[k][3],
                konto[k][4],
                konto[k][5]))


def konto_einzahlen():
    print("Geld auf Konto einzahlen")
    print("========================")
    print()
    konto_liste()

    print()
    kontonr = input(
        "Auf welches Konto wollen Sie einzahlen (Bitte Kontonummer angeben): ")
    betrag = float(input("Bitte einzuzahlender Betrag eingeben: "))
    konto[kontonr][1] += betrag
    print("Konto                   :", kontonr)
    print("Einbezahlt           Fr.: %.2f" % betrag)
    print("Aktueller Kontostand Fr.: %.2f" % konto[kontonr][1])
    print()
    input("Weiter mit Return")


def konto_auszahlen():
    print("Geld von Konto beziehen")
    print("========================")
    print()

    print("Ihr Code")


# Main block
validchoise = ("1", "2", "3", "4", "5", "6", "7", "q", "x")
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
    print("q  Ende")
    print()

    wahl = input("Ihre Wahl: ")
    now = datetime.datetime.now()
    jahr = now.strftime("%y")
    datum = now.strftime("%d.%m.%Y %H:%M:%S")

    if wahl not in validchoise:
        print(wahl, "ist eine ungültige Wahl")
        time.sleep(2)
        continue
    elif wahl == "1":
        kunde_erfassen()
    elif wahl == "2":
        print("Kundeninformationen anzeigen")
        print("====================")
        kunden_informationen()
        print()
        input("Weiter mit Return")
    elif wahl == "3":
        konto_erfassen()
    elif wahl == "4":
        konto_informationen()
    elif wahl == "5":
        '''Vorhandene Konten auflisten'''
        print("Vorhandene Kontonummern")
        print("=======================")
        print()
        konto_liste()
        print()
        input("Weiter mit Return")
    elif wahl == "6":
        konto_einzahlen()
    elif wahl == "7":
        konto_auszahlen()
    elif wahl == "x":
        test_daten_laden()
