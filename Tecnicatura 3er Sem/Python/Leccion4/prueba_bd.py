import psycopg2 # Esto es para poder conectarnos a PostgreSQl

# CREAMOS UN OBJETO DE TIPO CONEXION 
conexion = psycopg2.connect(
    user= 'postgres',
    password= '1604pt',
    host= '127.0.0.1',
    port= '5432',
    database= 'test_bd'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona' # consulta a la base de datos
cursor.execute(sentencia) # De esta manera ejecutamos la sentencia
registros = cursor.fetchall()   #Con METODO FECHALL, Y Recuperamos todos los registros que serán una lista
print(registros) # se muestran la lista de la base de datos creada en PostgreSQL 

# CEERRAMOS LA CONEXION CON LA BASE DE DATOS
cursor.close()  
conexion.close()