#Trasaciones clase 6 Manejo de transaciones manualmente
import psycopg2 as bd # Esto es para poder conectarnos a PostgreSQl

# CREAMOS UN OBJETO DE TIPO CONEXION 
conexion = bd.connect(user= 'postgres', password= '1604pt',host= '127.0.0.1', port= '5432',database= 'test_bd')
try:
    # conexion.autocommit = False # Desactivamos el modo autocommit (nose guardan los guardan  si nose hace commit) ESTO DIRECTAMENTE NO DEBERIA ESTAR
    cursor = conexion.cursor()  # Creamos un objeto cursor
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES (%s,%s,%s)'
    valores = ('Marta', 'Esparza', 'mesperza@gmail.com')
    cursor.execute(sentencia, valores)
    conexion.commit() # Hacemos commit manualmente
    print('Termina la transación')

except Exception as e: # Captura la exception
    conexion.rollback() # Hacemos rollback para deshacer los cambios
    print(f'Ocurrio un erorr, se hizo un rollback: {e}')
finally:
    conexion.close()