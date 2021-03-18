
##############################################
#
# Name: SuperBäcker_V1.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 30.01.2021
#
# Purpose: Übung mit einer Bäckerei
#
##############################################

#Preise
gipfeli=1.0
nussgipfel=2.0
zimtschnecke=1.5

# Keine Änderung ab hier mehr nötig ###########
summe=0                                                      #Variable summe auf 0 setzen
ende=''
print ("Wilkommen beim SuperBäcker:")                        #Willkommenstext anzeigen

while ende!='e':
   #Abfrage des Einkaufs
   gi=int(input("Anzahl Gipfeli     : "))                    #Anzahl Gipfelis abfragen
   ng=int(input("Anzahl Nussgipfel  : "))                    #Anzahl Nusgipfel abfragen
   zs=int(input("Anzahl Zimtschneken: "))                    #Anzahl Zimtschdnecken abfragen

   rechnung=(gi*gipfeli)+(nussgipfel*ng)+(zimtschnecke*zs)   #Berechnung Preis
   summe+=rechnung                                           #Aufrechnen der Summe
   print("Ihre Rechnung: Fr.", rechnung)                     #Anzeigen des Rechnungsbetrages
   print("Umsatz: Fr.", summe)                               #Anzeigen des Umsatzes
   print()
   ende=input("Nächster Kunde mit n, Ende mit e: ")          #Auf Eingabe warten
   if ende=='n':                                             #Die Meldung wollen wir nur bei Eingabe n sehen 
      print("Nächster Kunde ##############")

print("Auf Wiedersehen")

