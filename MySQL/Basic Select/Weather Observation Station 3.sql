-- Selects the name of the cities which the ID is an even number
SELECT DISTINCT CITY
FROM STATION
WHERE (ID % 2 = 0);