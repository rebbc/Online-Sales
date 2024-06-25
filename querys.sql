SELECT * FROM public."OnlineSales";

SELECT 
    "Product Category", 
    "Region", 
    SUM("Total Revenue") AS "Total Ventas"
FROM 
    "OnlineSales"
GROUP BY 
    "Product Category", 
    "Region"
ORDER BY 
    "Product Category", 
    "Region";



SELECT "Product Category", SUM("Total Revenue")
FROM "OnlineSales"
GROUP BY "Product Category";
