-- query_3.hql

USE flights_db;

-- Consulta para obtener el tiempo promedio de demora de las 5 aerolíneas con más vuelos
WITH top_5_airlines AS (
  SELECT Reporting_Airline, COUNT(*) AS Total_Flights
  FROM raw_flights_data
  GROUP BY Reporting_Airline
  ORDER BY Total_Flights DESC
  LIMIT 5
)

SELECT rf.Reporting_Airline,
       AVG(ArrDelay) AS Avg_Arrival_Delay
FROM raw_flights_data rf
JOIN top_5_airlines ta ON rf.Reporting_Airline = ta.Reporting_Airline
GROUP BY rf.Reporting_Airline
ORDER BY Avg_Arrival_Delay;
