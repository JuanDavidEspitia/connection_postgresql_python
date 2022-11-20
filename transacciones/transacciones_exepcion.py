import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Pepito', 'Perezlopes23567654', 'pepito@gmail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Pedro', 'Cardenaz', 'pedro@gmail.com', 9)
    conexion.commit()
    print(f'Termina la transaccion, se hizo commit')
except Exception as e:
    # En caso de una excepcion hace un rollback
    conexion.rollback()
    print(f'Ocurrió un error: {e}, de tipo {type(e)} y por tal razon se hizo rollback')
finally:
    conexion.close()