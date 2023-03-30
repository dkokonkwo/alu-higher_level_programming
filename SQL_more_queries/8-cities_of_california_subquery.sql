-- lists cities of Carlifornia
SELECT id, name FROM cities
WHERE states.id = (SELECT id FROM states WHERE name = 'Carlifornia')
ORDER BY id;
