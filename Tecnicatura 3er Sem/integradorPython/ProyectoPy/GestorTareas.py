from logger_base import log #

class Tarea:
    def __init__(self, id_tarea=None, descripcion=None, fecha=None, estado=None): #
        self._id_tarea = id_tarea
        self._descripcion = descripcion
        self._fecha = fecha
        self._estado = estado

    def __str__(self): #
        return f'''
            Id Tarea: {self._id_tarea},
            Descripción: {self._descripcion},
            Fecha Límite: {self._fecha},
            Estado: {self._estado}
        '''

    # Metodos Getters and Setters (properties)
    @property
    def id_tarea(self): #
        return self._id_tarea

    @id_tarea.setter
    def id_tarea(self, id_tarea): #
        self._id_tarea = id_tarea

    @property
    def descripcion(self): #
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion): #
        self._descripcion = descripcion

    @property
    def fecha(self): #
        return self._fecha

    @fecha.setter
    def fecha(self, fecha): #
        self._fecha = fecha

    @property
    def estado(self): #
        return self._estado

    @estado.setter
    def estado(self, estado): #
        self._estado = estado

    def append(self, tareas):
        pass


if __name__ == '__main__':
    # Ejemplos de uso de la clase Task
    tarea1 = Tarea(1, 'Estudiar Python', '2025-06-15', 'pendiente') #
    log.debug(tarea1) #

    tarea2 = Tarea(descripcion='Preparar informe', estado='completada') #
    log.debug(tarea2) #