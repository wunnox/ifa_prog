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

drop table if exists personen;
create table personen(
    id int primary key auto_increment,
    name varchar(30),
    funktion_id int,
    schiff_id int,
    constraint fk_schiff
    foreign key (schiff_id)
    references StarTrek_Schiffe(schiff_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
    );

insert into personen values(1, 'James T. Kirk',1,96);
insert into personen values(2, 'Jean-Luc Picard',1, 102);
insert into personen values(3, 'Spock',2,96);
insert into personen values(4, 'William T.Riker',2,102);
insert into personen values(5, 'Hikaru Sulu',3,96);
insert into personen values(6, 'Ro Laren',3,102);
insert into personen values(7, 'Pavel Chekov',4,96);
insert into personen values(8, 'Wesley Crusher',4,102);
insert into personen values(9, 'Montgomery Scott',5,96);
insert into personen values(10, 'Geordi LaForge',5,102);
insert into personen values(11, 'Dr. Leonard McCoy',6,96);
insert into personen values(12, 'Dr.Beverly Crusher',6,102);

