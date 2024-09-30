-- quality_rules_flightdate.hql

USE flights_db;

SELECT Div5WheelsOff, COUNT(*) as Cantidad
FROM raw_flights_data
GROUP BY Div5WheelsOff
ORDER BY Cantidad DESC
LIMIT 5;
