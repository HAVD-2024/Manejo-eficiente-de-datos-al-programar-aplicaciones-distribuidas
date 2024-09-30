-- query_1.hql
USE flights_db;

SELECT reporting_airline AS Airline, COUNT(*) AS Total_Flights
FROM raw_flights_data
GROUP BY reporting_airline
ORDER BY Total_Flights DESC
LIMIT 5;
