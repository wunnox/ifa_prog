##############################################
#
# Name: StartTrek_Procedure.sql
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.01.2021
#
# Purpose: Erstellt einen Procedure zum Einfügen eines Films
#
##############################################

DELIMITER //
CREATE PROCEDURE insert_film 
(
 IN titel VARCHAR(40),
 IN jahr int,
 IN kosten int,
 in schiff_id int,
 IN name VARCHAR(40)
) 

BEGIN
DECLARE id     INT DEFAULT 0;

insert ignore into schiff values(schiff_id,name);
insert into film values(id,titel,jahr,kosten,schiff_id);
END//
delimiter ;

call insert_film("Die dunkle Bedrohung",1999,115,6,"Millenium Falcon");
call insert_film("Angriff der Klonkrieger",2002,115,6,"Millenium Falcon");

#show procedure status;
