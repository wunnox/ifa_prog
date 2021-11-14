##############################################
#
# Name: StarWars.sql
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.10.2021
#
# Purpose: Tabelle und Daten für Beispiel StarWars
#
##############################################

#Inhalt Tabelle

drop table if exists StarWars;
create table StarWars(
    id int primary key auto_increment,
    Titel varchar(40),
    Jahr int,
    Kosten int,
    Raumschiff varchar(30));

insert into StarWars values(NULL,"Eine neue Hoffnung",1977,11,"Millennium Falcon");
insert into StarWars values(NULL,"Das Imperium schlägt zurück",1980,18,"Millennium Falcon");
insert into StarWars values(NULL,"Die Rückkehr der Jedi-Ritter",1983,32,"Millennium Falcon");
insert into StarWars values(NULL,"Die dunkle Bedrohung",1999,115,"Millennium Falcon");
insert into StarWars values(NULL,"Angriff der Klonkrieger",2002,115,"Millennium Falcon");
insert into StarWars values(NULL,"Die Rache der Sith",2005,113,"Millennium Falcon");
insert into StarWars values(NULL,"Das Werwachen der Macht",2015,245,"Millennium Falcon");
insert into StarWars values(NULL,"Rouge One",2016,200,"Millennium Falcon");
insert into StarWars values(NULL,"The Last Jedi",2017,200,"Millennium Falcon");
insert into StarWars values(NULL,"Solo",2018,275,"Millennium Falcon");
insert into StarWars values(NULL,"The Rise of Skywalker",2019,275,"Millennium Falcon");

