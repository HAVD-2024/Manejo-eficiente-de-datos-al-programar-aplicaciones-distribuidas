-- quality_rules_flightdate.hql

USE flights_db;


SELECT FlightDate, COUNT(*) as Cantidad
FROM raw_flights_data
GROUP BY FlightDate
ORDER BY Cantidad DESC
LIMIT 5;
