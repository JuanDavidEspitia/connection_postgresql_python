import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')

try:
    # Esta sentencia permite que no se guarde automaticamente los cambios o la sentencia
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Maira', 'Esperanza', 'maria@gmail.com')
    cursor.execute(sentencia, valores)
    # Con esta sentencia guardamos, lo ideal es que el commit lo hagamos en el codigo manualmente
    conexion.commit()
    print(f'Termina la transaccion')
except Exception as e:
    # En caso de una excepcion hace un rollback
    conexion.rollback()
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()