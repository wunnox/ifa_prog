#############################################
#
# Name: Enterprise_normalisiert.sql
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.01.2021
#
# Purpose: Datenbank mit normalisierten Tabellen von Raumschiff Enterprise
#
##############################################

# Datenbank erstellen
create database if not exists Enterprise;
use Enterprise;

drop table if exists film;
create table film(
    id int primary key auto_increment,
    titel varchar(40),
    jahr int,
    kosten int,
    schiff_id int);

insert into film values(NULL, 'Star Trek: Der Film', 1979, 35,1);
insert into film values(NULL, 'Der Zorn des Khan', 1982, 11,1);
insert into film values(NULL, 'Auf der Suche nach Mr. Spock', 1984, 17,1);
insert into film values(NULL, 'Zurück in die Gegenwart', 1986, 25,1);
insert into film values(NULL, 'Am Rande des Universums', 1989, 30,1);
insert into film values(NULL, 'Das unentdeckte Land', 1991, 30,1);
insert into film values(NULL, 'Treffen der Generationen', 1994, 35,2);
insert into film values(NULL, 'Der erste Kontakt', 1996, 45,2);
insert into film values(NULL, 'Der Aufstand', 1998, 58,2);
insert into film values(NULL, 'Nemesis', 2002, 60,2);
insert into film values(NULL, 'Star Trek', 2009, 150,1);
insert into film values(NULL, 'Into Darkness', 2013, 190,1);
insert into film values(NULL, 'Beyond', 2016, 185,1);

# Tabellen erstellen
drop table if exists person;
create table person(
    id int primary key auto_increment,
    name varchar(30),
    funktion_id int,
    schiff_id int);

insert into person values(NULL, 'James T. Kirk',1,1);
insert into person values(NULL, 'Jean-Luc Picard',1, 2);
insert into person values(NULL, 'Spock',2,1);
insert into person values(NULL, 'William T.Riker',2,2);
insert into person values(NULL, 'Hikaru Sulu',3,1);
insert into person values(NULL, 'Ro Laren',3,2);
insert into person values(NULL, 'Pavel Chekov',4,1);
insert into person values(NULL, 'Wesley Crusher',4,2);
insert into person values(NULL, 'Montgomery Scott',5,1);
insert into person values(NULL, 'Geordi LaForge',5,2);
insert into person values(NULL, 'Dr. Leonard McCoy',6,1);
insert into person values(NULL, 'Dr.Beverly Crusher',6,2);

drop table if exists schiff;
create table schiff(
    id int primary key auto_increment,
    name varchar(30));

insert into schiff values(1, 'Enterprise NCC-1701');
insert into schiff values(2, 'Enterprise NCC-1701-E');
insert into schiff values(3, 'Antares NCC-501');
insert into schiff values(4, 'Aurora NC-17740');
insert into schiff values(5, 'Yorkshire NCC-330');

drop table if exists funktion;
create table funktion(
    id int primary key auto_increment,
    funktion varchar(20));

insert into funktion values(NULL,'Captain');
insert into funktion values(NULL,'ErsterOffizier');
insert into funktion values(NULL,'Navigation');
insert into funktion values(NULL,'Steuerung');
insert into funktion values(NULL,'Chefingenieur');
insert into funktion values(NULL,'MedOffizier');
