##############################################
#
# Name: Outer_Join_Beispiele.sql
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.01.2021
#
# Purpose: Tabelle und Daten für Beispiel mit Outer Join
#
##############################################

drop table if exists Standort;
create table Standort(
    StandortID int primary key auto_increment,
    Stadt varchar(40));

insert into Standort values(1, 'Bern');
insert into Standort values(2, 'Basel');
insert into Standort values(3, 'Zürich');
insert into Standort values(4, 'Lausanne');
insert into Standort values(5, 'Genf');

drop table if exists Abteilung;
create table Abteilung(
    AbteilungID int primary key auto_increment,
    Strasse varchar(20),
    StandortID int,
    Name varchar(20));

insert into Abteilung values(21, "Genfergasse 6",1,"Verkauf");
insert into Abteilung values(24, "Zollgasse 12",1,"Verwaltung");
insert into Abteilung values(27, "Av. du Grey 110",4,"Wartung");
insert into Abteilung values(29, "Rue du Garre 45",5,"Lager");

drop table if exists Mitarbeiter;
create table Mitarbeiter(
    MitarbeiterID int primary key auto_increment,
    AbteilungID int,
    Name varchar(30));

insert into Mitarbeiter values(61, 24,"Meier");
insert into Mitarbeiter values(63, 27,"Maillard");
insert into Mitarbeiter values(64, 27,"Jaquet");
insert into Mitarbeiter values(65, 24,"Kaufmann");
insert into Mitarbeiter values(66, 21,"Roggli");
insert into Mitarbeiter values(67, 29,"Poretti");
insert into Mitarbeiter values(68, 21,"Fischer");
insert into Mitarbeiter values(69, 21,"Berset");
insert into Mitarbeiter values(70, 29,"Brunner");
insert into Mitarbeiter values(71, 21,"Hofer");
insert into Mitarbeiter values(72, 21,"Blaser");
