SELECT CONCAT(Name,"(", LEFT(Occupation, 1),")")
FROM OCCUPATIONS
ORDER BY Name;
-- The string should be "There are a total of [occupation_count] [occupation]s."
SELECT CONCAT("There are a total of ", COUNT(Occupation), " ", LOWER(Occupation), "s.") AS Total
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY Total;