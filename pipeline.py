# Librerías

import pandas as pd
from sqlalchemy import create_engine

# Carga de datos

df = pd.read_csv('Online Sales Data.csv')

# Configuración de la conexión

usuario = 'postgres'
contraseña = 'pola'
host = 'localhost'
puerto = '5432'
nombre_base_datos = 'OnlineSales'

# Conexión a PostgreSQL

connection_string = f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{nombre_base_datos}'
engine = create_engine(connection_string)


# Transformación de sugenrencia: calcular el precio total si no está presente como columna

if 'Total Revenue' not in df.columns:
    df['Total Revenue'] = df['Units Sold'] * df['Unit Price']


# Conversión de la columna 'Date' a tipo de dato datetime.

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')


# Carga de los datos en PostgreSQL

table_name = 'OnlineSales'  
df.to_sql(table_name, engine, if_exists='replace', index=False)

print("Datos guardados en la base de datos.")