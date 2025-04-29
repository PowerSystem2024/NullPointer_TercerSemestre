from ManejoArchivos import ManejoArchivos

# MANEJO DE CONTEXTO (manager) WITH: sintaxis simplificad, abre y cierra el archivo
#with open('prueba.txt','r', encoding= 'utf8') as archivo: 
#    print(archivo.read())

# NO hace falta ni el try, ni el finally
# enel contexto de with lo que se ejecuta de manera automatica
# Utiliza diferentes métodos: __enter__este es el que abre
# Ahora el siguiente método es el que cierra: __exit__

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
