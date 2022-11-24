import sys
from psycopg2 import pool
from logger_base import log

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1 # Minimo numero de conexiones
    _MAX_COM = 5 # Maximo numero de conexiones a la BD
    _pool = None

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None: # Preguntamos si la variable ya ha sido inicializada
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_COM,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._PORT,
                                                      database=cls._DATABASE
                                                      )
                log.debug(f'Ceracion del Pool Exitosa,  {cls._pool}')
                return cls._pool

            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()

        else:
            # En caso de que no sea none, retornamos el objeto
            return cls._pool


    @classmethod
    def obtener_conexion(cls):
       conexion = cls.obtener_pool().getconn() # Regresa un objeto de conexion de la BD
       log.debug(f'Conexion obtenida del pool: {conexion}')
       return conexion


    @classmethod
    def librerar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion) # Retorna el objeto conexion que ya no esta usando el usuario al pool
        log.debug(f'Regresamos la conexion al Pool: {conexion}')

    @classmethod
    def cerrar_pool_conexiones(cls):
        """
        Metodo que se encarga de cerrar todos los objetos de conexion en nuestro pool
        :return:
        """
        cls.obtener_pool().closeall()
        log.debug(f'Cerramos todas las conexiones del Pool')



if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    Conexion.librerar_conexion(conexion1)

    conexion2 = Conexion.obtener_conexion()
    conexion3 = Conexion.obtener_conexion()
    conexion4 = Conexion.obtener_conexion()
    conexion5 = Conexion.obtener_conexion()
    # Con la 6 conexion exedemos el maximo de conexiones
    # conexion6 = Conexion.obtener_conexion()
    Conexion.cerrar_pool_conexiones()





