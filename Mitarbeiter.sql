##############################################
#
# Name: Mitarbeiter.sql
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.01.2021
#
# Purpose: Tabelle und Daten für Beispiel Normalisierung
#
##############################################

#Grundform
drop table if exists Mitarbeiter;
create table Mitarbeiter(
    id int primary key auto_increment,
    Name varchar(40),
    aid int,
    Abteilung varchar(30),
    Wohnort varchar(30));

insert into Mitarbeiter values(1,"Hans Meier",2,"Verkauf","3000 Bern");
insert into Mitarbeiter values(2,"Anna Muster",3,"Marketing","8000 Zürich");
insert into Mitarbeiter values(3,"Jean Dupont",3,"Marketing","3000 Bern");
insert into Mitarbeiter values(4,"Mario Rossi",4,"Vertrieb","8000 Zürich");

#Erste Normalform
drop table if exists Mitarbeiter_1N;
create table Mitarbeiter_1N(
    id int primary key auto_increment,
    Vorname varchar(40),
    Nachname varchar(40),
    aid int,
    Abteilung varchar(30),
    PLZ int,
    Wohnort varchar(30));

insert into Mitarbeiter_1N values(1,"Hans","Meier",2,"Verkauf",3000,"Bern");
insert into Mitarbeiter_1N values(2,"Anna", "Muster",3,"Marketing",8000,"Zürich");
insert into Mitarbeiter_1N values(3,"Jean", "Dupont",3,"Marketing",3000,"Bern");
insert into Mitarbeiter_1N values(4,"Mario", "Rossi",4,"Vertrieb",8000,"Zürich");

#Zweite Normalform
drop table if exists Mitarbeiter_2N;
create table Mitarbeiter_2N(
    id int primary key auto_increment,
    Vorname varchar(40),
    Nachname varchar(40),
    aid int,
    PLZ int,
    Wohnort varchar(30));

drop table if exists Abteilung;
create table Abteilung(
    aid int primary key auto_increment,
    Abteilung varchar(30));

insert into Mitarbeiter_2N values(1,"Hans","Meier",2,3000,"Bern");
insert into Mitarbeiter_2N values(2,"Anna", "Muster",3,8000,"Zürich");
insert into Mitarbeiter_2N values(3,"Jean", "Dupont",3,3000,"Bern");
insert into Mitarbeiter_2N values(4,"Mario", "Rossi",4,8000,"Zürich");

insert into Abteilung values(1,"Buchhaltung");
insert into Abteilung values(2,"Verkauf");
insert into Abteilung values(3,"Marketing");
insert into Abteilung values(4,"Vertrieb");

#Dritte Normalform
drop table if exists Mitarbeiter_3N;
create table Mitarbeiter_3N(
    id int primary key auto_increment,
    Vorname varchar(40),
    Nachname varchar(40),
    aid int,
    oid int);

drop table if exists Wohnort;
create table Wohnort(
    oid int primary key auto_increment,
    PLZ int,
    Wohnort varchar(30));

insert into Mitarbeiter_3N values(1,"Hans","Meier",2,1);
insert into Mitarbeiter_3N values(2,"Anna", "Muster",3,2);
insert into Mitarbeiter_3N values(3,"Jean", "Dupont",3,1);
insert into Mitarbeiter_3N values(4,"Mario", "Rossi",4,2);

insert into Wohnort values(1,3000,"Bern");
insert into Wohnort values(2,8000,"Zürich");
