-- select only records with name value
-- in secod_table

SELECT `score`, `name`
FROM second_table
WHERE `name` IS NOT NULL AND `name` != ''
ORDER BY `score` DESC, `NAME` ASC;
