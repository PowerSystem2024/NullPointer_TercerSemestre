import psycopg2 # Esto es para poder conectarnos a PostgreSQl

# CREAMOS UN OBJETO DE TIPO CONEXION 
conexion = psycopg2.connect(user= 'postgres', password= '1604pt',host= '127.0.0.1', port= '5432',database= 'test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor: # El uso del With permite cerrar la conexion automaticamente
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE ide_persona = %s' # Sentencia SQL para actualizar
            valores = (
                ('Juan', 'Roz', 'jroz@gmail.com',4),
                ('Romina', 'Ayala','ayalar@gmail.com',8)
            )# Esto es una tupla 
            cursor.executemany(sentencia, valores) # De esta manera ejecutamos la sentencia para muchos
            registros_actualizados= cursor.rowcount  # Rowcout se da marcha atras a intento de la insercion de datos
            print(f'Los registros actualizados son: {registros_actualizados}')
            
except Exception as e: # Captura la exception
    print(f'Ocurrio un error: {e}') 
finally:
    conexion.close()