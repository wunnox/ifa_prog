#!/usr/local/bin/python3
##############################################
#
# Name: SuperBäcker_G_V1.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 30.01.2021
#
# Purpose: Bäckerei Applikation mit GUI
#
##############################################

from tkinter import *

#Preise
gipfeli = 1.0
nussgipfel=2.0
zimtschnecke = 1.5
summe=0

def buttonEndeClick():
    # Beenden
    tkFenster.destroy()

def buttonBerechnenClick():
    global summe

    # Übernahme der Daten
    anzgipfeli = float(entryGipfeli.get())
    anznussgipfel = float(entryNussgipfel.get())
    anzzimtschnecke = float(entryZimtschnecke.get())

    # Verarbeitung der Daten
    rechnung = (gipfeli*anzgipfeli)+(nussgipfel*anznussgipfel)+(zimtschnecke*anzzimtschnecke)
    rechnunganzeige = str(round(rechnung*10)/10)
    summe+=rechnung
    summeanzeige=str(summe)

    # Anzeige der Daten
    labelRechnung.config(text=rechnunganzeige)
    labelSumme.config(text=summeanzeige)

# Hauptfenster
tkFenster = Tk()
tkFenster.title('SuperBäcker')
tkFenster.geometry('300x300')

#Standardgrössen für Widgets
artikelwidth=160
artikelheight=27
artikelx=54
artikely=24
preiswidth=40
preisheight=artikelheight
preisx=215
preisy=artikely

# Artikel Gipfeli
labelGipfeli = Label(master=tkFenster, text='Anzahl Gipfeli:')
labelGipfeli.place(x=artikelx, y=artikely, width=artikelwidth, height=artikelheight)
# Preis Gipfeli
entryGipfeli = Entry(master=tkFenster, bg='#EBEBEB')
entryGipfeli.place(x=preisx, y=preisy, width=preiswidth, height=preisheight)

# Artikel Nussgipfel
labelNussgipfel = Label(master=tkFenster, text='Anzahl Nussgipfel:')
labelNussgipfel.place(x=artikelx, y=artikely+40, width=artikelwidth, height=artikelheight)
# Preis Nussgipfel
entryNussgipfel = Entry(master=tkFenster, bg='#EBEBEB')
entryNussgipfel.place(x=preisx, y=preisy+40, width=preiswidth, height=preisheight)

# Artikel Zimtschnecke
labelZimtschnecke = Label(master=tkFenster, text='Anzahl Zimtschnecken:')
labelZimtschnecke.place(x=artikelx, y=artikely+80, width=artikelwidth, height=artikelheight)
# Preis Zimtschnecke
entryZimtschnecke = Entry(master=tkFenster, bg='#EBEBEB')
entryZimtschnecke.place(x=preisx, y=preisy+80, width=preiswidth, height=preisheight)

# Button zum Berechnen
buttonBerechnen = Button(master=tkFenster, bg='#CCE5FF', activebackground='#3399FF', text='Abrechnung', relief="raised", command=buttonBerechnenClick)
buttonBerechnen.place(x=artikelx, y=144, width=200, height=artikelheight)

# Rechnung
labelRechnungBetrag = Label(master=tkFenster, bg='#D5E88F', text='Ihre Rechnung:')
labelRechnungBetrag.place(x=artikelx, y=184, width=artikelwidth, height=artikelheight)
# Ausgabe Rechnung
labelRechnung = Label(master=tkFenster, bg='#E0E0E0', text='')
labelRechnung.place(x=preisx, y=184, width=preiswidth, height=artikelheight)

# Umsatz
labelSummeT = Label(master=tkFenster, bg='#D5E88F', text='Umsatz:')
labelSummeT.place(x=artikelx, y=224, width=artikelwidth, height=artikelheight)
# Ausgabe Rechnung
labelSumme = Label(master=tkFenster, bg='#E0E0E0', text='')
labelSumme.place(x=preisx, y=224, width=preiswidth, height=artikelheight)

# Button zum Beenden
buttonBerechnen = Button(master=tkFenster, text='Ende', relief="raised", bg='#FF9999',command=buttonEndeClick)
buttonBerechnen.place(x=artikelx, y=264, width=200, height=artikelheight)

# Aktivierung des Fensters
tkFenster.mainloop()
