SELECT DISTINCT CITY FROM STATION
WHERE CITY NOT RLIKE '^[aeiou]' OR CITY NOT RLIKE '[aeiou]$'