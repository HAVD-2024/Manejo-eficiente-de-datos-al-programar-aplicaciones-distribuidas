-- quality_rules_flightdate.hql

USE flights_db;

SELECT COUNT(*) AS count
FROM raw_flights_data
WHERE FlightDate = '2024-01-25';
