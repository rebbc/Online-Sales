# Online-Sales

En este documento se presenta la documentación técnica del proyecto Online-Sales. Este proyecto se centra en la integración, procesamiento, almacenamiento y análisis de datos de ventas en línea. El objetivo principal es proporcionar una visión detallada del pipeline de datos implementado, los procesos ETL utilizados, y cómo estos datos se visualizan para obtener insights valiosos. A continuación, se detallarán las herramientas y tecnologías utilizadas, la metodología seguida para la carga y transformación de los datos, la estructura y el diccionario de la base de datos, así como las consultas SQL y visualizaciones realizadas con PowerBI. En la parte inferior, encontrarán las visualizaciones y las consultas realizadas en PostgreSQL.

# Documentación técnica

## Pipeline
En este apartado desarrollaré el procesamiento, carga y almacenamiento de los datos. Las herramientas utilizadas fueron Pyhton, PostgreSQL y PowerBI para las visualizaciones, y las librerías Pandas y SQLalchemy para la conexión a la base de datos.

### Carga y transformación de datos

- Fuentes de Datos: Los datos de ventas se recopilaron de un archivo CSV ('Online Sales Data.csv').

- Tranformación: Se implementaron procesos ETL para transformar los datos, ya que no requeria una limpieza significativa. Esto incluye la conversión de tipos de datos, y mantener la columna 'Total Revenue' con los resultados correctos (sujeto a la transformación sugerida en el proyecto). Aseguré que las columnas tengan el tipo de datos correcto, por ejemplo, convertir fechas a tipo datetime, cantidades a int y precios a float.

- Carga: Se realizaron scripts de Python utilizando bibliotecas como Pandas para la lectura y carga de datos en una base de datos PostgreSQL. Se emplearon conexiones específicas, asegurando la correcta autenticación y manejo de errores. Se implementó una carga incremental que solo actualiza los registros nuevos o modificados. El código proporcionado permite que se registren grandes volúmenes de datos de ventas. 

### Almacenamiento

- Base de Datos: Los datos se almacenaron en una base de datos PostgreSQL, diseñada con una estructura que facilita la consulta y el análisis. Creé una tabla específica para almacenar los de datos de ventas, las columnas se crearon en PostgreSQL antes de la carga.  

- Conexión a DB: En el primer apartado del archivo 'pipeline.py' ingresé la configuración y conexión a PostgreSQL. En caso de haber algún inconveniente, no seguiría con el proceso de ETL. Esto considero que es útil para detectar este tipo de errores con tiempo, ahorrando recursos.

## Diccionario y estructura de datos

La fuente proporcionada consta de las siguientes columnas: 

- Transaction ID: (int) ID de la transacción.
- Date: (datetime) fecha de la transacción.
- Product Category: (object) categoría del producto.
- Product Name: (object) nombre del producto.
- Units Sold: (int) cantidades en unidades.
- Unit Price: (float) valor del producto por unidad.
- Total Revenue: (float) valor total de la transacción.
- Region: (object) región del comprador.
- Payment Method: (object) medio de pago utilizado. 

# Visualización de datos

Para la visualización utilicé PowerBI, conectando con el archivo CSV de manera local. En la primer imagen podemos ver el dashboard sin ningun filtro. Grafiqué las ventas medidas en cantidad de dinero, por meses y por día (para poder conocer cuáles son las fechas con mayor y menor cantidad de ventas), esto nos permite conocer tendencias de ventas. En el primer gráfico circular, podemos ver las ventas por categorías de los productos, contabilizado en cantidad de dinero. Por último, en el gráfico circular inferior, podemos ver los medios de pago utilizados, permitiendonos conocer cómo operan nuestros clientes y dándonos la posibilidad de ofrecer promociones bancarias/financieras para generar más ventas. En la parte superior del dashboard están los filtros por región y por trimestre. En las imágenes siguientes, se verá la interacción. 
<br><br>

Haciendo un breve análisis, podemos ver que luego del primer trimestre, las ventas fueron disminuyendo. Esto puede sugerirnos cambios en la demanda a lo largo del año. 
<br>
En cuanto a las categorías más vendidas, se destaca un mayor volumen de ventas en productos tecnológicos, incluyendo electrónica y electrodomésticos para el hogar. Este hallazgo sugiere que estos segmentos de productos son especialmente populares entre nuestros clientes. 
<br>
Además, se observa que en la región de Asia, los clientes muestran una preferencia marcada por realizar transacciones utilizando tarjetas de débito y crédito. Este conocimiento puede ser aprovechado para adaptar las estrategias de pago y mejorar la experiencia del cliente, por ejemplo, ofreciendo promociones o descuentos específicos para transacciones con tarjeta.
<br>
En resumen, el análisis inicial revela tanto áreas de éxito como oportunidades de mejora. 
<br><br>
<img src = 'img/Visualizacion 1.png' height = '600'>
<br><br>

- Filtro por Región: En este caso, aplicamos el filtro por región.
<br>
<img src = 'img/Visualizacion 2.png' height = '600'>
<br><br>

- Filtros por Región y Trimestre: Aplicamos ambos filtros, por región y por trimestre.
<br>
<img src = 'img/Visualizacion 3.png' height = '600'>
<br><br><br>
Esta visualización nos permite conocer tendencias de ventas, saber cómo operan nuestros clientes y cuales son sus categorías de preferencia. 

# Consultas SQL

<img src = 'img/primer consulta .png' height = '600'>
<br><br>
<img src = 'img/segunda consulta.png' height = '600'>
<br><br>
Para optimizar la consulta proporcionada, eliminé la línea 'WHERE "Total Revenue" IS NOT NULL"', ya que considero que si se encuentra un dato nulo, no lo podría sumar. Es una línea redundante y no es necesaria para la consulta. 