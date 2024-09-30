-- quality_rules_flightdate.hql

USE flights_db;

SELECT DepDelayMinutes, COUNT(*) as Cantidad
FROM raw_flights_data
GROUP BY DepDelayMinutes
ORDER BY Cantidad DESC
LIMIT 5;
