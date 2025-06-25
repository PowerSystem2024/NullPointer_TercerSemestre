from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self): 
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del méyodo with y __enter_-')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()  # Assuming obtenerConexion() returns a public connection object
        return self._cursor

    def __exit__(self, tipo_exception, valor_exception, detalle_exception):
        log.debug('Se ejecuta el método exit')
        if valor_exception:
            self._conexion.rollback()
            log.debug(f'Ocurrió una excepción: {valor_exception}')
        else:
            self._conexion.commit()# hace un comit
            log.debug('Commit de la transaccion')
            self._cursor.close() #cierra la conexion 
            Conexion.liberarConexion(self._conexion)

if __name__ =='__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
