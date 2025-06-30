from GestorTareas import Tarea  # Importa la clase Tarea
from TipoTarea import TaskDAO  # Importa la clase TaskDao
from SGPersonal import Conexion, log  # Importa tu clase Conexion y el logger
from datetime import datetime  # Todavía se necesita para el manejo de fechas en la CLI

class TareaCLI:
    """
    Implementa la interfaz de línea de comandos para el gestor de tareas.
    Utiliza TaskDAO para interactuar con la base de datos.
    """

    def __init__(self):
        """
        Inicializa la CLI. No se necesitan pasar gestores como antes,
        ya que TaskDAO y Conexion son clases con métodos de clase (classmethod)
        y la lógica de conexión está encapsulada en Conexion.
        """
        pass

    def main_menu(self):
        """
        Muestra el menú principal de la aplicación.
        """
        print("\n--- Gestor de Tareas Personales ---")
        print("1. (Re)Crear Tabla de Tareas (Ejecutar solo la primera vez o si es necesario)")
        print("2. Añadir nueva tarea")
        print("3. Ver todas las tareas")
        print("4. Ver tareas pendientes")
        print("5. Ver tareas completadas")
        print("6. Marcar tarea como completada")
        print("7. Eliminar tarea")
        print("8. Salir")
        print("----------------------------------")

    def run_app(self):
        """
        Ejecuta el bucle principal de la aplicación CLI.
        """
        while True:
            self.main_menu()
            choice = input("Elige una opción: ").strip()

            if choice == '1':
                # Aquí, implementamos la creación directamente llamando a un cursor.
                conn = Conexion.obtenerConexion()
                if conn:
                    try:
                        with Conexion.obtenerCursor() as cur:
                            cur.execute("""
                                CREATE TABLE IF NOT EXISTS tarea (
                                    id SERIAL PRIMARY KEY,
                                    descripcion TEXT NOT NULL,
                                    fecha DATE,
                                    estado VARCHAR(20) DEFAULT 'pendiente'
                                );
                            """)
                            conn.commit()
                            log.info("Tabla 'tarea' creada o ya existente.")
                    except Exception as e:
                        log.error(f"Error al crear la tabla 'tarea': {e}")
            elif choice == '2':
                descripcion = input("Introduce la descripción de la tarea: ").strip()
                if not descripcion:
                    print("La descripción no puede estar vacía.")
                    continue
                due_date_str = input("Introduce la fecha límite (YYYY-MM-DD, opcional): ").strip()
                fecha = None
                if due_date_str:
                    try:
                        fecha = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                    except ValueError:
                        print("Formato de fecha inválido. La fecha límite no se establecerá.")

                # Crear un objeto Tarea y pasarlo al DAO
                nueva_tarea = Tarea(descripcion=descripcion, fecha=fecha, estado='pendiente')
                TaskDAO.insertar(nueva_tarea)
            elif choice == '3':
                lista_tareas = TaskDAO.seleccionar()
                if not lista_tareas:
                    log.info("No hay tareas para mostrar.")
                    continue
                log.info("\n--- Todas las Tareas ---")
                for tarea_individual in lista_tareas:
                    log.info(tarea_individual)
                log.info("--------------------------")
            elif choice == '4':
                lista_pendientes = TaskDAO.seleccionar(status='pendiente')
                if not lista_pendientes:
                    log.info("No hay tareas pendientes.")
                    continue
                log.info("\n--- Tareas Pendientes ---")
                for tarea_individual in lista_pendientes:
                    log.info(tarea_individual)
                log.info("--------------------------")
            elif choice == '5':
                lista_completadas = TaskDAO.seleccionar(status='completada')
                if not lista_completadas:
                    log.info("No hay tareas completadas.")
                    continue
                log.info("\n--- Tareas Completadas ---")
                for tarea_individual in lista_completadas:
                    log.info(tarea_individual)
                log.info("--------------------------")
            elif choice == '6':
                try:
                    id_tarea = int(input("Introduce el ID de la tarea a marcar como completada: "))
                    # Crear un objeto Tarea con el ID y el estado 'completada'
                    tarea_a_actualizar = TaskDAO.seleccionar_por_id(id_tarea)

                    if tarea_a_actualizar:
                        tarea_a_actualizar.estado = 'completada'
                        TaskDAO.actualizar(tarea_a_actualizar)
                        log.info(f"Tarea con ID {id_tarea} marcada como completada.")
                    else:
                        log.warning(f"No se encontró ninguna tarea con ID {id_tarea}.")
                except ValueError:
                    print("ID de tarea inválido. Por favor, introduce un número.")
            elif choice == '7':
                try:
                    id_tarea= int(input("Introduce el ID de la tarea a eliminar: "))
                    # Crear un objeto Tarea con solo el ID para eliminar
                    tarea_a_eliminar = Tarea(id_tarea=id_tarea)
                    rows_deleted = TaskDAO.eliminar(tarea_a_eliminar)
                    if rows_deleted > 0:
                        log.info(f"Tarea con ID {id_tarea} eliminada correctamente")
                    else:
                        log.warning(f"No se encontro ninguna tarea con ID {id_tarea} para eliminar.")
                except ValueError:
                    print("ID de tarea inválido. Por favor, introduce un número.")
            elif choice == '8':
                log.info("¡Chau!")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    # La clase Conexion gestiona su propia instancia de conexión y cursor de forma singleton.
    # Los métodos de TaskDAO son @classmethod, por lo que no necesitamos una instancia de TaskDAO.

    # Creamos una instancia de la CLI
    cli_app = TareaCLI()

    # Ejecutamos la aplicación
    cli_app.run_app()