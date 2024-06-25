from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
import pandas as pd

df = pd.read_csv('Online Sales Data.csv')

usuario = 'postgres'
contraseña = 'pola'
host = 'localhost'
puerto = '5432'
nombre_base_datos = 'postgres'

connection_string = f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{nombre_base_datos}'
engine = create_engine(connection_string)

try:
    connection = engine.connect()
    print("Conexión exitosa")
    connection.close()
except Exception as e:
    print(f"Error de conexión: {e}")


# Definir la metadata
metadata = MetaData()

# Definir la tabla
mi_tabla = Table('mi_tabla', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('quantity', Integer),
                 Column('price_per_unit', Float),
                 Column('total_price', Float),
                 Column('discounted_price', Float),
                 Column('order_date', String),
                 Column('quantity_normalized', Float)
                )

# Crear la tabla en la base de datos
metadata.create_all(engine)

# Transformación de sugenrencia: calcular el precio total si no está presente como columna

if 'Total Revenue' not in df.columns:
    df['Total Revenue'] = df['Units Sold'] * df['Unit Price']


# Conversión de la columna 'Date' a tipo de dato datetime.

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')


# Guardar los datos en PostgreSQL
table_name = 'OnlineSales'  
df.to_sql(table_name, engine, if_exists='replace', index=False)

print("Datos guardados en la base de datos con éxito.")