import psycopg2 # Esto es para poder conectarnos a PostgreSQl

# ELIMINAR VARIOS REGISTROS DE DATOS de una sola vez

# CREAMOS UN OBJETO DE TIPO CONEXION 
conexion = psycopg2.connect(user= 'postgres', password= '1604pt',host= '127.0.0.1', port= '5432',database= 'test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor: # El uso del With permite cerrar la conexion automaticamente
            sentencia = 'DELETE FROM persona WHERE ide_persona IN %s ' # Sentencia para elimminar
            entrada = input('Digite los números de registo a eliminar(separados por coma): ')
            valores = (tuple(entrada.split(',')),) # tupla de tuplas 
            cursor.execute(sentencia, valores) # De esta manera ejecutamos 
            registros_eliminados= cursor.rowcount  # Rowcout se da marcha atras a intento de la insercion de datos
            print(f'Los registros eliminados son: {registros_eliminados}')
            
except Exception as e: # Captura la exception
    print(f'Ocurrio un error: {e}') 
finally:
    conexion.close()