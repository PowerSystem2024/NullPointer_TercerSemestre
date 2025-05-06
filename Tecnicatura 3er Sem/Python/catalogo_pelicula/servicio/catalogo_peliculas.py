# sercicio/CatalogoPeliculas

import os # operanting sistem

class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt' # 

    @classmethod
    def agregar_peliculas(cls ,pelicula): #cls: es una convencion para referirse a la clase dentro de un metodo de clase, permite  modificar atributoos y crear instancias de manenera controlada
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding= 'utf8') as archivo:
            print(f'Catalogo de Peliculas' .center(50,'-'))  
            print(archivo.read()) # Todas las lista de peliculas se leeran 

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}') # Archivo eliminado


