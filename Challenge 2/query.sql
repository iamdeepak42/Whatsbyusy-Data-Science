SELECT first_name, last_name
	FROM
(SELECT b.first_name, b.last_name 
FROM table_1 a
JOIN manager b
ON a.id_table_1 = b.id_manager
WHERE a.dt_work_from => ‘2020-01-01’  AND a.dt_work_to  =< ‘2020-01-30’

UNION

SELECT b.first_name, b.last_name 
FROM table_1 a
JOIN employee c
ON a.id_table_1 = c.id_employee
WHERE a.dt_work_from => ‘2020-01-01’  AND a.dt_work_to  =< ‘2020-01-30’)
