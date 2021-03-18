create database if not exists banky;
use banky

drop table if exists banky_konto;
create table banky_konto(
    kontonr varchar(20) primary key,
    kontostand float(8,2),
    kunden_id int,
    kontotyp_id int,
    erstellt datetime,
    letzteaenderung datetime);

drop table if exists banky_kunden;
create table banky_kunden(
    kunden_id int primary key auto_increment,
    anrede varchar(20),
    vorname varchar(20),
    nachname varchar(50),
    adresse varchar(50),
    wohnort varchar(50),
    erstellt datetime,
    letzteaenderung datetime);

drop table if exists banky_kontotyp;
create table banky_kontotyp(
    kontotyp_id int primary key auto_increment,
    kontotyp varchar(30),
    kontobeschreibung varchar(100));

drop table if exists banky_transaktion;
create table banky_transaktion(
    trans_id int primary key auto_increment,
    kontonr varchar(20),
    betrag float(8,2),
    kontostand float(8,2),
    datum datetime);
