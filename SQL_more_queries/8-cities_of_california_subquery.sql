-- lists cities of Carlifornia
SELECT `id`, `name` FROM `cities` WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = "California") ORDER BY `id` ASC;
