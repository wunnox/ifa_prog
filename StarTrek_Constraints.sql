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
# Purpose: Erstellt die Tabelle film mit einem constraint foreign key auf die Tabelle schiff
#
##############################################

drop table if exists film;
create table film(
  id int primary key auto_increment,
  titel varchar(40),
  jahr int,
  kosten int,
  schiff_id int,
  constraint fk_schiff foreign key (schiff_id) references schiff(id) 
    ON UPDATE CASCADE ON DELETE SET NULL
);

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

