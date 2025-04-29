
#Declaramos una variable
# NO! OLVIDAR... para poner asentos debemos poner = encoding = 'utf8'
archivo = None
try:
    archivo = open('prueba.txt' , 'w',encoding = 'utf8') # La w es de la write que significa escribir CON ESTO TAMBIEN CREAMOS UN ARCHIVO TXT
    archivo.write('Programamos con diferentes tipos de archivo, ahora en txt.\n')
    archivo.write('Los asentos son importantes para las palabras.\n')
    archivo.write('como por ejemplo:  acción, ejecución y producción. \n')
    archivo.write('Las letras son: \n r(read, LEER),\n a(apend, ANEXA),\n w(write, ESCRIBE),\n x (crea, CREAR ARCHIVO)')
    archivo.write('\n t (text, ESTO ES PARA TEXTO), \n b (ARCHIVOS COMBINADOS), \n w+ y r+ son iguales biseversa (LEER Y ESCRIBIR)\n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('\nCon esto terminamos')
except Exception as e:
    print(f'Error: {e}') # Muestra el error si ocurre
finally: # siempre se ejecuta este bloque
    if archivo: # verifica que'archivo no sea None'
        archivo.close() # con esto, cerra el archivo si fue abierto

# archivo.write('Todo quedo perfecto'): este es un error, no podemos trabajar
#  con un archivo ya cerrado, sino que este dentro del orden 