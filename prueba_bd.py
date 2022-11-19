import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')
print(conexion)

# Creamos un Cursor
"""
Un cursor es: es un objeto que nos permite ejecutar sentecias SQL en postgresql
"""

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()

print(registros)


# Cerramos la conexion a la BBDD
cursor.close()
conexion.close()