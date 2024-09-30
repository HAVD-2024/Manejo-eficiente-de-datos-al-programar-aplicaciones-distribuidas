-- quality_rules_flightdate.hql

USE flights_db;

SELECT OriginAirportID, COUNT(*) as Cantidad
FROM raw_flights_data
GROUP BY OriginAirportID
ORDER BY Cantidad DESC
LIMIT 5;
