-- quality_rules_flightdate.hql

USE flights_db;

SELECT DestAirportID, COUNT(*) as Cantidad
FROM raw_flights_data
GROUP BY DestAirportID
ORDER BY Cantidad DESC
LIMIT 5;
