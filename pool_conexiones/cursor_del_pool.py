from logger_base import log
from pool_conexiones.conexion import Conexion


class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del metodo With __enter__')
        # Obtenemos un objeto de tipo conexion
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detallle_excepcion):
        # Metodo que se manda a llamar cuando termina el metodo with
        log.debug('Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una execpcion, se hace rollback: {valor_excepcion} {tipo_excepcion} {detallle_excepcion}')
        else:
            # Guardamos los cambios en la base de datos
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.librerar_conexion(self._conexion)


if __name__ == '__main__':
    """
    Con el with, indirectamente llamamos el metodo __enter__ y cuando se cierra el with estamos llamando
    el metodo __exit__
    """
    with CursorDelPool() as cursor:
        log.debug(f'Dentro del bloque With')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())