##############################################
#
# Name: Enterprise_Basis.sql
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.01.2021
#
# Purpose: Tabelle und Daten für Beispiel StarTrek
#
##############################################

#Inhalt Tabelle
#Nr.,"Titel",Jahr,Kosten,"Raumschiff","Captain","Erster Offizier","Navigation","Steuerung","Chefingenieur","Medizin. Offizier")

drop table if exists StarTrek;
create table StarTrek(
    id int primary key auto_increment,
    Titel varchar(40),
    Jahr int,
    Kosten int,
    Raumschiff varchar(30),
    Captain varchar(30),
    ErsterOffizier varchar(30),
    Navigation varchar(30),
    Steuerung varchar(30),
    Chefingenieur varchar(30),
    MedOffizier varchar(30));

insert into StarTrek values(1,"Star Trek: Der Film",1979,35,"USS Enterprise NCC-1701","James T. Kirk","Spock","Hikaru Sulu","Pavel Chekov","Montgomery Scott","Dr. Leonard McCoy");
insert into StarTrek values(2,"Der Zorn des Khan",1982,11,"USS Enterprise NCC-1701","James T. Kirk","Spock","Hikaru Sulu","Pavel Chekov","Montgomery Scott","Dr. Leonard McCoy");
insert into StarTrek values(3,"Auf der Suche nach Mr. Spock",1984,17,"USS Enterprise NCC-1701","James T. Kirk","Spock","Hikaru Sulu","Pavel Chekov","Montgomery Scott","Dr. Leonard McCoy");
insert into StarTrek values(4,"Zurück in die Gegenwart",1986,25,"USS Enterprise NCC-1701","James T. Kirk","Spock","Hikaru Sulu","Pavel Chekov","Montgomery Scott","Dr. Leonard McCoy");
insert into StarTrek values(5,"Am Rande des Universums",1989,30,"USS Enterprise NCC-1701","James T. Kirk","Spock","Hikaru Sulu","Pavel Chekov","Montgomery Scott","Dr. Leonard McCoy");
insert into StarTrek values(6,"Das unentdeckte Land",1991,30,"USS Enterprise NCC-1701","James T. Kirk","Spock","Hikaru Sulu","Pavel Chekov","Montgomery Scott","Dr. Leonard McCoy");
insert into StarTrek values(7,"Treffen der Generationen",1994,35,"USS Enterprise NCC-1701-E","Jean-Luc Picard","William T. Riker","Ro Laren","Wesley Crusher","Geordi LaForge","Dr. Beverly Crusher");
insert into StarTrek values(8,"Der erste Kontakt",1996,45,"USS Enterprise NCC-1701-E","Jean-Luc Picard","William T. Riker","Ro Laren","Wesley Crusher","Geordi LaForge","Dr. Beverly Crusher");
insert into StarTrek values(9,"Der Aufstand",1998,58,"USS Enterprise NCC-1701-E","Jean-Luc Picard","William T. Riker","Ro Laren","Wesley Crusher","Geordi LaForge","Dr. Beverly Crusher");
insert into StarTrek values(10,"Nemesis",2002,60,"USS Enterprise NCC-1701-E","Jean-Luc Picard","William T. Riker","Ro Laren","Wesley Crusher","Geordi LaForge","Dr. Beverly Crusher");
insert into StarTrek values(11,"Star Trek",2009,150,"USS Enterprise NCC-1701","James T. Kirk","Spock","Hikaru Sulu","Pavel Chekov","Montgomery Scott","Dr. Leonard McCoy");
insert into StarTrek values(12,"Into Darkness",2013,190,"USS Enterprise NCC-1701","James T. Kirk","Spock","Hikaru Sulu","Pavel Chekov","Montgomery Scott","Dr. Leonard McCoy");
insert into StarTrek values(13,"Beyond",2016,185,"USS Enterprise NCC-1701","James T. Kirk","Spock","Hikaru Sulu","Pavel Chekov","Montgomery Scott","Dr. Leonard McCoy");
