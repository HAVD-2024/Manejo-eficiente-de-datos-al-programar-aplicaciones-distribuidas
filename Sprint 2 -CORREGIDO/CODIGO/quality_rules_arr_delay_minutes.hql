-- quality_rules_flightdate.hql

USE flights_db;

SELECT ArrDelayMinutes, COUNT(*) as Cantidad
FROM raw_flights_data
GROUP BY ArrDelayMinutes
ORDER BY Cantidad DESC
LIMIT 5;
