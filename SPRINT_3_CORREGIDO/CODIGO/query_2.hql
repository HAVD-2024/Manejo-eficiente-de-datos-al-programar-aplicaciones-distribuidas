-- query_2.hql
USE flights_db;

-- Consulta para obtener el top 10 de aerolíneas con mayor efectividad de llegada a tiempo
SELECT Reporting_Airline, 
       SUM(CASE WHEN ArrDelay <= 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS OnTime_Percentage
FROM raw_flights_data
GROUP BY Reporting_Airline
ORDER BY OnTime_Percentage DESC
LIMIT 10;
