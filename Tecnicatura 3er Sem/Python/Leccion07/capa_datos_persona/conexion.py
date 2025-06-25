from psycopg2 import pool
# psycopg2 as db otra manera de importar el psycopg2
from capa_datos_persona.logger_base import log
import sys

class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = '1604pt'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerConexion(cls):
       conexion = cls.obtenerPool().getconn() # este método se encarga de regresar una conexión hacia la bdd
       log.debug(f'Conexión obtenida del pool: {conexion}')
       return conexion

    @classmethod
    def obtenerCursor(cls):
        pass

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def liberarConexion(cls,conexion): #metodo para liberar la conexion
        cls.obtenerPool().putconn(conexion) #volver a poner la conexion 
        log.debug(f'Regresamos la conexion del pool: {conexion}') 

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall() # este método cierra todas las conexiones del pool
        log.debug('Se han cerrado todas las conexiones del pool')

        # Nota: 
        # El pool de conexiones es una forma de manejar conexiones a la base de datos de manera eficiente.
        # En lugar de abrir y cerrar conexiones cada vez que se necesita interactuar con la base de datos, 
        # se crea un pool que mantiene un conjunto de conexiones abiertas y las reutiliza según sea necesario.


# El metodo se llama para liberar este objeto, recibir un objeto de conexion y regesarlo al pool de conexiones para que otro lo pueda usar. 
        # si no se libera la conexion, se queda ocupada y no se puede usar por otro objeto.


if __name__== '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1) # liberamos la conexión
    conexion2 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion2)
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion() # nos excedemos en una conexión
 
  

 
