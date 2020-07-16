-- Selects the rounded sum of the two columns "LAT_N" and "LONG_W" to 2 decimal places
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) FROM STATION;
