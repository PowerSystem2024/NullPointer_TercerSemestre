#Declaramos una variable
try:
    archivo = open('prueba.txt', 'w',encoding='utf8') #la W es de write que significa escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecucíon y producción\n')
    archivo.write('las letras son: \nr read leer, \na append anexa, \nwrite escribe, \nxcrea un archivo')
    archivo.write('\nt esta es para texto o text, \nb archivo binarios, \nw+ lee y escribe r+\n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: #SIEMPRE SE EJECUTA
    archivo.close() #con esto se debe cerrar el archivo
# archivo.write('Todo quedo perfecto') este es un error

