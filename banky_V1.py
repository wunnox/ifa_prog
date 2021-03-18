##############################################
#
# Name: banky_V1.py
#
# Author: Peter Christen
#
# Version: 0.1
#
# Date: 25.02.2021
#
# Purpose: Kontoverwaltungsprogramm
#
##############################################

# Benötigte Module
import datetime   # Datumsanzeige
import time
import os

# Variablen
kundennr = 0
wahl = 0
kunde = {}

while wahl != 'q':
    # Menupunkt zur Auswahl der Aktivitäten
    os.system("clear")
    print("Applikation Banky")
    print("=================")
    print()
    print("1. Kunde erfassen")
    print("2. Kundeninformationen anzeigen")
    print("3. Konto erfassen")
    print("q Ende")
    print()

    wahl = input("Ihre Wahl: ")

    now = datetime.datetime.now()
    jahr = now.strftime("%y")
    datum = now.strftime("%d.%m.%Y %H:%M:%S")

    if wahl == "1":
        print("Kunde erfassen")
        print("==============")
        print()
        kundennr += 1
        vorname = input("Vorname: ")
        nachname = input("Nachname: ")
        wohnort = input("Wohnort: ")
        kunde[kundennr] = [vorname, nachname, wohnort, datum]

        print()
        print("Folgender Kunde wurde erfasst:")
        print("==============================")
        print()
        print("Kundennr  : ", kundennr)
        print("Vorname    : ", vorname)
        print("Nachname   : ", nachname)
        print("Wohort     : ", wohnort)
        print("Erfasst am : ", datum)
        print()
        print(kunde)
        input("Weiter mit Return")

    elif wahl == "2":
        print("Kundeninformationen anzeigen")
        print("============================")
        print()
        print("{0:<5}{1:<15}{2:<20}{3:<20}".format(
            "ID", "Vorname", "Nachname", "Wohnort"))
        for k in kunde.keys():
            print(
                "{0:<5}{1:<15}{2:<20}{3:<20}".format(
                    k,
                    kunde[k][0],
                    kunde[k][1],
                    kunde[k][3]))
        print()
        input("Weiter mit Return")

    elif wahl == "3":
        print("Konto wird erfasst")
        time.sleep(1)
    elif wahl == 'q':
        pass
    else:
        print(wahl, "ist keine gültige Auswahl")
        time.sleep(2)
