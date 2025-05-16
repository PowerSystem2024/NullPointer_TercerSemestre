import psycopg2 # Esto es para poder conectarnos a PostgreSQl

# CREAMOS UN OBJETO DE TIPO CONEXION 
conexion = psycopg2.connect(user= 'postgres', password= '1604pt',host= '127.0.0.1', port= '5432',database= 'test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor : # El uso del With permite cerrar la conexion automaticamente
            sentencia = 'SELECT * FROM persona WHERE ide_persona IN %s' # consulta a la base de datos, Placeholder
            entrada = input('Digite los ide_personsa a buscar (separados por coma):')
            llaves_primarias = (tuple(entrada.split( ',' )),) #poner "coma" para hacerlo tupla en parametros
            cursor.execute(sentencia, llaves_primarias) # De esta manera ejecutamos la sentencia
            registros = cursor.fetchall()   # Recuperamos todos los registros que serán una lista
            for registro in registros: 
                print(registro) # se muestran la lista de la base de datos creada en PostgreSQL 
except Exception as e: # Captura la exception
    print(f'Ocurrio un error: {e}') 
finally:
    conexion.close()

# fetchall: obtiene TODOS LOS REGISTROS de la consulta y los devuleve como una lista de tuplas
# fetchone: obtiene un SOLO UN REGISTRO 