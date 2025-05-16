import psycopg2 # Esto es para poder conectarnos a PostgreSQl

# ELIMINAR REGISTROS DE DATOS 

# CREAMOS UN OBJETO DE TIPO CONEXION 
conexion = psycopg2.connect(user= 'postgres', password= '1604pt',host= '127.0.0.1', port= '5432',database= 'test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor: # El uso del With permite cerrar la conexion automaticamente
            sentencia = 'DELETE FROM persona WHERE ide_persona=%s ' # Sentencia para elimminar
            entrada = input('Digite el número de registo a eliminar: ')
            valores = (entrada,) # esto es una tupla de valores
            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia 
            registros_eliminados= cursor.rowcount  # Rowcout se da marcha atras a intento de la insercion de datos
            print(f'Los registros eliminados son: {registros_eliminados}')
            
except Exception as e: # Captura la exception
    print(f'Ocurrio un error: {e}') 
finally:
    conexion.close()