#!/Users/peter/opt/anaconda3/bin/python3
##############################################
#
# Name: banky_tabellen.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.03.2021
#
# Purpose: Erstellt alle Tabellen für die Applikation banky
#
##############################################

import mysql.connector

def datenbank_neu_erstellen():
   # Mit Datenbank verbinden
   connection = mysql.connector.connect(
       user='root',
       password='newpassword',
       host='localhost')
   cursor2 = connection.cursor()

   #Datenbank und Tabellen erstellen
   cursor2.execute("create database if not exists banky")
   cursor2.execute("use banky")

   print("Erstelle banky_konto")
   cursor2.execute("drop table if exists banky_konto")
   cursor2.execute("create table banky_konto( kontonr varchar(20) primary key, kontostand float(8,2), kunden_id int, kontotyp_id int, erstellt datetime, letzteaenderung datetime)")

   print("Erstelle banky_kunden")
   cursor2.execute("drop table if exists banky_kunden")
   cursor2.execute("create table banky_kunden( kunden_id int primary key auto_increment, anrede varchar(20), vorname varchar(20), nachname varchar(50), adresse varchar(50), wohnort varchar(50), erstellt datetime, letzteaenderung datetime)")

   print("Erstelle banky_kontotyp")
   cursor2.execute("drop table if exists banky_kontotyp")
   cursor2.execute("create table banky_kontotyp( kontotyp_id int primary key auto_increment, kontotyp varchar(30), kontobeschreibung varchar(100))")

   print("Erstelle banky_transaktion")
   cursor2.execute("drop table if exists banky_transaktion")
   cursor2.execute("create table banky_transaktion( trans_id int primary key auto_increment, kontonr varchar(20), betrag float(8,2), kontostand float(8,2), datum datetime)")

   #Änderungen sichern und Datenbank schliessen
   connection.commit()
   cursor2.close()

if __name__=='__main__':
    datenbank_neu_erstellen()
