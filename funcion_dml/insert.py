import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Jose', 'Lara', 'jose@gmail.com')
            cursor.execute(sentencia, valores)
            # conexion.commit()   --> Se hace automaticamente por el metodo Open
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()