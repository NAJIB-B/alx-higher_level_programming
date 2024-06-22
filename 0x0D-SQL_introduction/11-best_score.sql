-- showing all the record of second table
-- in descending order

SELECT `score`, `name`
FROM `second_table`
WHERE `score` > 9
ORDER BY `score` DESC;
