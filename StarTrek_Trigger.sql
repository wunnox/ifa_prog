##############################################
#
# Name: StartTrek_Trigger.sql
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 10.01.2021
#
# Purpose: Erstellt einen Trigger zum Einfügen von Schiffen
#
##############################################

delimiter // 
create trigger FilmTrigger before insert on film
  for each row
  begin
  insert ignore into schiff(id, name) values (new.schiff_id, NULL);
end//
delimiter ;

insert into film values(NULL,'Das Imperium schlägt zurück',1980,18,6);
insert into film values(NULL,'Die Rückkehr der Jedi-Ritter',1983,32,6);
