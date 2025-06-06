import psycopg2 # Esto es para poder conectarnos a PostgreSQl

# CREAMOS UN OBJETO DE TIPO CONEXION 
conexion = psycopg2.connect(user= 'postgres', password= '1604pt',host= '127.0.0.1', port= '5432',database= 'test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor: # El uso del With permite cerrar la conexion automaticamente
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s,%s)'
            valores = (
                ('Carlos', 'Lara', 'Clara@gamil.com'),
                ('Marcos','Canto', 'mcanro@gmail.com'),
                ('Miguel', 'Cadenas', 'miguelC@gmail.com')
            )# Esto es una tupla 
            cursor.executemany(sentencia, valores) # De esta manera ejecutamos la sentencia para muchos
            #conexion.commit() # Esto es para guardar los cambios en la base de datos.
            registros_insertados = cursor.rowcount  # Recuperamos todos los registros que serán una lista. Rowcout se da marcha atras a intento de la insercion de datos
            print(f'Los registros insertados son: {registros_insertados}')
except Exception as e: # Captura la exception
    print(f'Ocurrio un error: {e}') 
finally:
    conexion.close()