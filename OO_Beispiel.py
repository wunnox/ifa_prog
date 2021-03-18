
##############################################
#
# Name: OO_Beispiel.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 20.11.2015
#
# Purpose: Beispiel eines Object Oriented Python Scripts
#
##############################################

#Module
import os

# Variablen
auto = {}

# Klassen
class Auto:
    def __init__(self, marke):
        self.marke = marke
        self.sitze = 0
        self.speed = 0

    def auto_erfassen(self,sitze,speed):
        self.sitze=sitze
        self.speed=speed

    def auto_anzeigen(self):
        print("{0:<10}{1:^6}{2:>6}".format(self.marke, self.sitze, self.speed))

    def fahrzeit_berechnen(self,distanz):
        dauer=distanz/self.speed
        print("Die Fahrzeit mit dem Auto %s für die Distanz von %s Kilometer dauert %.2f Stunden" % (self.marke,distanz,dauer))

# Main Script
a=[0]
c=1
while True:
    os.system("clear")
    eingabe = input('-> ')

    if eingabe == '1':
        print("Auto: erfassen")
        marke = input('Marke: ')
        sitze = input('Sitze: ')
        speed = input('Geschweindigkeit: ')
        auto[marke] = Auto(marke)
        auto[marke].auto_erfassen(sitze,speed)
    elif eingabe == '2':
        print("Vorhandene Autos:")
        print("{0:<10}{1:<6}{2:<6}".format("Marke","Size","Geschwindigkeit"))
        for marke in auto.keys():
            auto[marke].auto_anzeigen()
        input("Weiter mit Return")
    elif eingabe == '3':
        print("Fahrzeit berechnen:")
        ap = int(input('Anzahl Personen: '))
        distanz = int(input('Distanz in Kilometer: '))
        print("Verfügbare Fahrzeuge:")
        for m in auto.keys():
            if auto[m].sitze >= ap:
                print(c, m)
                a.append(m)
                c+=1
        m = int(input('Ihre Auswahl: '))
        marke = a[m]
        auto[marke].fahrzeit_berechnen(distanz)
        input("Weiter mit Return")
    elif eingabe == 'x':
        auto['Volvo'] = Auto('Opel')
        auto['Volvo'].auto_erfassen(4,180)
        auto['VW-Bus'] = Auto('VW Bus')
        auto['VW-Bus'].auto_erfassen(8,140)
        auto['Topolino'] = Auto('Topolino')
        auto['Topolino'].auto_erfassen(4,100)
        auto['Lotus'] = Auto('Lotus')
        auto['Lotus'].auto_erfassen(2,200)
    elif eingabe == 'e':
        break
