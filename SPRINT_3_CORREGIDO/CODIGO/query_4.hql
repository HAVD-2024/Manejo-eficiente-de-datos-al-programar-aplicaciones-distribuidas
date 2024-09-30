-- query_3.hql

USE flights_db;

SELECT 
    SUM(CASE WHEN ArrDelay <= 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS OnTime,
    SUM(CASE WHEN CarrierDelay > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS AirCarrierDelay,
    SUM(CASE WHEN WeatherDelay > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS WeatherDelay,
    SUM(CASE WHEN NASDelay > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS NASDelay,
    SUM(CASE WHEN SecurityDelay > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS SecurityDelay,
    SUM(CASE WHEN LateAircraftDelay > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS AircraftArrivingLate,
    SUM(CASE WHEN Cancelled = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS Cancelled,
    SUM(CASE WHEN Diverted = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS Diverted
FROM 
    raw_flights_data
WHERE 
    FlightDate BETWEEN '2024-03-01' AND '2024-03-31'; -- Rango de fechas según tus datos
