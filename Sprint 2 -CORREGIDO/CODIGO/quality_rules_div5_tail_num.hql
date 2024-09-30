-- quality_rules_flightdate.hql

USE flights_db;

SELECT Div5TailNum, COUNT(*) as Cantidad
FROM raw_flights_data
GROUP BY Div5TailNum
ORDER BY Cantidad DESC
LIMIT 5;
