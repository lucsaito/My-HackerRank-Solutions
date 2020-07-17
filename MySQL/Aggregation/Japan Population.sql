-- Selects the sum of all the Japanese population
SELECT SUM(POPULATION) FROM CITY
WHERE COUNTRYCODE = "JPN";