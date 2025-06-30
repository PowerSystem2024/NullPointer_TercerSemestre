from GestorTareas import Tarea # Importa la clase GestorTareas
from SGPersonal import Conexion # Importa tu clase Conexion
from logger_base import log #

class TaskDAO:
    """
    DAO para el objeto Task.
    Define operaciones CRUD para la tabla 'tasks'.
    """
    _SELECCIONAR = 'SELECT id, description, due_date, status FROM tasks ORDER BY id'
    _SELECCIONAR_CON_FILTRO = 'SELECT id, description, due_date, status FROM tasks WHERE status = %s ORDER BY id'  # Nueva para claridad
    _SELECCIONAR_POR_ID = 'SELECT id, description, due_date, status FROM tasks WHERE id = %s'  # Correcto para seleccionar por ID
    _INSERTAR = 'INSERT INTO tasks (description, due_date, status) VALUES (%s,%s,%s) RETURNING id' #
    _ACTUALIZAR = 'UPDATE tasks SET description=%s, due_date=%s, status=%s WHERE id=%s' #
    _ELIMINAR = 'DELETE FROM tasks WHERE id=%s' #

    @classmethod
    def seleccionar(cls, status=None):
        """
        Selecciona todas las tareas o filtra por estado.
        """
        conn = None
        cursor = None
        lista_tareas = []

        try:
            conn = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()

            if status:
                cursor.execute(cls._SELECCIONAR_CON_FILTRO, (status,))
            else:
                cursor.execute(cls._SELECCIONAR) #

            registros = cursor.fetchall() #
            for registro in registros:
                # Se asume el orden de las columnas en la consulta SELECT
                tarea_obj = Tarea(registro[0], registro[1], registro[2], registro[3]) #
                lista_tareas.append(tarea_obj) #
        except Exception as e:
            log.error(f'Error al seleccionar tareas: {e}')
        finally:
            # En la clase Conexion, los atributos _conexion y _cursor son estáticos
            # y no se cierran automáticamente con 'with'.
            # Para una aplicación de CLI, la reconexión en cada operación puede ser aceptable,
            # pero para aplicaciones web o de larga duración, querrías una gestión de pool de conexiones.
            # Aquí, confiamos en el singleton de Conexion.
            pass # No cerramos la conexión aquí ya que Conexion la gestiona de forma global.
        return lista_tareas #

    @classmethod
    def seleccionar_por_id(cls, id_tarea):  # Este método es EXCLUSIVAMENTE para UN ID
        """
        Selecciona una tarea por su ID.
        Retorna un objeto Tarea si se encuentra, None en caso contrario.
        """
        conn = None
        cursor = None
        tarea = None  # Inicializamos como None

        try:
            conn = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            cursor.execute(cls._SELECCIONAR_POR_ID, (id_tarea,))  #
            registro = cursor.fetchone()  #

            if registro:
                tarea = Tarea(registro[0], registro[1], registro[2], registro[3])
        except Exception as e:
            log.error(f'Error al seleccionar tarea por ID: {e}')
        finally:
            pass
        return tarea

    @classmethod
    def insertar(cls, tarea: Tarea):
        """
        Inserta una nueva tarea en la base de datos.
        Retorna el ID de la tarea insertada o 0 si falla.
        """
        conn = None
        cursor = None
        inserted_id = 0

        try:
            conn = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor() #
            valores = (tarea.descripcion, tarea.fecha, tarea.estado if tarea.estado else 'pendiente') #
            cursor.execute(cls._INSERTAR, valores) #
            inserted_id = cursor.fetchone()[0] # Obtener el ID de la tarea recién insertada
            tarea.id_tarea = inserted_id
            conn.commit()
            log.debug(f'Tarea Insertada: {tarea}') #
            return inserted_id
        except Exception as e:
            log.error(f'Error al insertar tarea: {e}')
            if conn:
                conn.rollback() # Hacer rollback en caso de error
        finally:
            pass # Conexión gestionada por Conexion.obtenerConexion/Cursor
        return inserted_id #


    @classmethod
    def actualizar(cls, tarea: Tarea):
        """
        Actualiza una tarea existente en la base de datos.
        """
        conn = None
        cursor = None
        rows_updated = 0

        try:
            conn = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor() #
            valores = (tarea.descripcion, tarea.fecha, tarea.estado, tarea.id_tarea) #
            cursor.execute(cls._ACTUALIZAR, valores) #
            conn.commit()
            rows_updated = cursor.rowcount #
            log.debug(f'Tarea actualizada: {tarea}') #
        except Exception as e:
            log.error(f'Error al actualizar tarea: {e}')
            if conn:
                conn.rollback() # Hacer rollback en caso de error
        finally:
            pass # Conexión gestionada por Conexion.obtenerConexion/Cursor
        return rows_updated #

    @classmethod
    def eliminar(cls, tarea: Tarea):
        """
        Elimina una tarea de la base de datos.
        """
        conn = None
        cursor = None
        rows_deleted = 0

        try:
            conn = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor() #
            valores = (tarea.id_tarea,) #
            cursor.execute(cls._ELIMINAR, valores) #
            conn.commit()
            rows_deleted = cursor.rowcount #
            log.debug(f'Tarea eliminada: {tarea}') #
        except Exception as e:
            log.error(f'Error al eliminar tarea: {e}')
            if conn:
                conn.rollback() # Hacer rollback en caso de error
        finally:
            pass # Conexión gestionada por Conexion.obtenerConexion/Cursor
        return rows_deleted #

if __name__ == '__main__':

    # Seleccionar todas las tareas
    tasks = TaskDAO.seleccionar()
    for task in tasks:
        log.debug(task)

