# Dominio/pelicula.py

class Pelicula:
    def __init__(self, nombre:str): # METODO CONTRCUCTOR (__init__). Atributo: nombre , de tipo str(string)
        self._nombre = nombre # almacena el valor del argumento[nombre] en el atributo _nombre del objeto

    def __str__(self): # METODO REPRESENTACIÓN EN CADENA, Define como se mostrara un objeto de Pelicula cuando se imprima
        return (f'Pelicula: {self._nombre}') # devuelve una cadena que incluye el nombre de la pelicula
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter # 
    def nombre(self, nombre): #definie como se modifica el atributo_nombre
        self._nombre = nombre