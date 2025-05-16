import psycopg2

try:
    conn = psycopg2.connect(
        dbname='PUBLICIDAD',
        user='postgres',
        password='29609295Ammi#',
        host='10.21.5.188',
        port='5432'
    )
    print("Conexión exitosa")
except Exception as e:
    print(f"Error de conexión: {e}")