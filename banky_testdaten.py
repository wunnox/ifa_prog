##############################################
#
# Name: Name: banky_testdaten.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.03.2021
#
# Purpose: Testdaten für banky-Applikation
#
##############################################

def test_daten_laden(cursor,datum):
    '''Laden von Daten zum Testen'''

    # Tabellen entleeren
    cursor.execute("delete from banky_kunden")
    cursor.execute("delete from banky_konto")
    cursor.execute("delete from banky_transaktion")
    cursor.execute("delete from banky_kontotyp")

    # Testdaten Kunden laden
    cursor.execute("insert into banky_kunden values(%s,%s,%s,%s,%s,%s,%s,%s)",(1, 'Herr', 'Hans', 'Muster', 'Kramgasse 4', '3000 Bern', datum,datum))
    cursor.execute("insert into banky_kunden values(%s,%s,%s,%s,%s,%s,%s,%s)",(2, 'Frau', 'Anna', 'Meier', 'Plantetenweg 8', '3110 Münsingen', datum,datum))
    cursor.execute("insert into banky_kunden values(%s,%s,%s,%s,%s,%s,%s,%s)",(3, 'Herr', 'Remo', 'Müller', 'Finkenweg 20', '3006 Elfenau', datum,datum))
    cursor.execute("insert into banky_kunden values(%s,%s,%s,%s,%s,%s,%s,%s)",(4, 'Frau', 'Irene', 'Moser', 'Scheuermatt 12', '3013 Rubigen', datum,datum))
    cursor.execute("insert into banky_kunden values(%s,%s,%s,%s,%s,%s,%s,%s)",(5, 'Herr', 'Peter', 'Christen', 'Steinackerstrasse 17','3184 Wünnewil', datum,datum))

    #Kontotypen laden
    cursor.execute("insert into banky_kontotyp values(%s,%s,%s)", (1, 'Privatkonto', 'Konto für natürliche Personen'))
    cursor.execute("insert into banky_kontotyp values(%s,%s,%s)", (2, 'Sparkonto', 'Sparkonto für natürliche Personen'))
    cursor.execute("insert into banky_kontotyp values(%s,%s,%s)", (3, 'Kontokorrent', 'Konto für juristische Personen'))

    #Testdaten Konten laden
    cursor.execute("insert into banky_konto values(%s,%s,%s,%s,%s,%s)", ('12345-21', 1200.00, 1, 1, datum, datum))
    cursor.execute("insert into banky_transaktion values(%s,%s,%s,%s,%s)", (0, '12345-21', 1200.00, 1200.00, datum))
    cursor.execute("insert into banky_konto values(%s,%s,%s,%s,%s,%s)", ('12346-21', 3200.00, 2, 1, datum, datum))
    cursor.execute("insert into banky_transaktion values(%s,%s,%s,%s,%s)", (0, '12346-21', 3200.00, 3200.00, datum))
    cursor.execute("insert into banky_konto values(%s,%s,%s,%s,%s,%s)", ('12347-21', 221.00, 3, 1, datum, datum))
    cursor.execute("insert into banky_transaktion values(%s,%s,%s,%s,%s)", (0, '12347-21', 221.00, 221.00, datum))
    cursor.execute("insert into banky_konto values(%s,%s,%s,%s,%s,%s)", ('12348-21', 50.20, 4, 1, datum, datum))
    cursor.execute("insert into banky_transaktion values(%s,%s,%s,%s,%s)", (0, '12348-21', 50.20, 50.20, datum))
    cursor.execute("insert into banky_konto values(%s,%s,%s,%s,%s,%s)", ('12349-21', 1200.00, 5, 1, datum, datum))
    cursor.execute("insert into banky_transaktion values(%s,%s,%s,%s,%s)", (0, '12349-21', 1200.00, 1200.00, datum))

