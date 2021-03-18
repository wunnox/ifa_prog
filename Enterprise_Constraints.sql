#############################################
#
# Name: Enterprise_Constraints.sql
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.01.2021
#
# Purpose: Erstellt die Tabelle person mit einem constraint foreign key auf die Tabelle schiff
#
##############################################

drop table if exists schiff;
create table schiff(
    schiff_id int primary key auto_increment,
    name varchar(30));

drop table if exists person;
create table person(
    id int primary key auto_increment,
    name varchar(30),
    funktion_id int,
    schiff_id int,
    constraint fk_schiff
    foreign key (schiff_id)
    references schiff(schiff_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    );

insert into schiff values(NULL, 'U.S.S. Enterprise NCC-1701');
insert into schiff values(NULL, 'USS Enterprise NCC-1701-E');

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

