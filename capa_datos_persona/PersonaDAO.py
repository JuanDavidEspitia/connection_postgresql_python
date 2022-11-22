from capa_datos_persona.Persona import Persona
from conexion_bd import ConexionBD
from logger_base import log

class PersonaDAO:
    """
    DAO (Data Access Object)
    CRUD (Create, Read, Update, Delete
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) values(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WhERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with ConexionBD.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with ConexionBD.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                log.debug(f'Persona a insertar: {persona}')
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with ConexionBD.obtener_conexion():
            with ConexionBD.obtener_cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona Actualizada: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with ConexionBD.obtener_conexion():
            with ConexionBD.obtener_cursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Persona Eliminada: {persona}')
                return cursor.rowcount


if __name__ == '__main__':

    # Inserta un registro
    # persona1 = Persona(nombre='Camilo', apellido='Duque', email='camilo@gmail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Cantidad de Personas Insertadas: {personas_insertadas}')

    # Actualizar un registro
    # persona2 = Persona(id_persona=15, nombre='Salome', apellido='Espitia', email='salome@gmail.com')
    # personas_actulizadas = PersonaDAO.actualizar(persona2)
    # log.debug(f'Cantidad de Personas Actualizadas: {personas_actulizadas}')


    # Eliminar un registro
    persona3 = Persona(id_persona=16)
    personas_eliminar = PersonaDAO.actualizar(persona3)
    log.debug(f'Cantidad de Personas eliminadas: {personas_eliminar}')

    # Seleccionar objetos
    list_personas = PersonaDAO.seleccionar()
    for persona in list_personas:
        log.debug(persona)
