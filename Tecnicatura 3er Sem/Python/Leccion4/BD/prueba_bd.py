import psycopg2 # Esto es para poder conectarnos a PostgreSQl

# CREAMOS UN OBJETO DE TIPO CONEXION 
conexion = psycopg2.connect(user= 'postgres', password= '1604pt',host= '127.0.0.1', port= '5432',database= 'test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor : # El uso del With permite cerrar la conexion automaticamente
            sentencia = 'SELECT * FROM persona WHERE ide_persona = %s' # consulta a la base de datos, Placeholder
            ide_persona = input('Digite un número para el ide_persona: ')
            cursor.execute(sentencia, (ide_persona,)) # De esta manera ejecutamos la sentencia
            registros = cursor.fetchone()   #Con METODO FECHALL, Y Recuperamos todos los registros que serán una lista
            print(registros) # se muestran la lista de la base de datos creada en PostgreSQL 
except Exception as e: # Captura la exception
    print(f'Ocurrio un error: {e}') 
finally:
    conexion.close()

# https://www.psycopg.org/docs/usage.html

# fetchall: obtiene TODOS LOS REGISTROS de la consulta y los devuleve como una lista de tuplas
# fetchone: obtiene un SOLO UN REGISTRO 