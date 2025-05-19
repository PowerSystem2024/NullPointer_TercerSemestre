# CLASE 6 POR ULTIMO CON WITH (aplicando las buenas practicas)

import psycopg2 as bd # Esto es para poder conectarnos a PostgreSQl

# CREAMOS UN OBJETO DE TIPO CONEXION 
conexion = bd.connect(user= 'postgres', password= '1604pt',host= '127.0.0.1', port= '5432',database= 'test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:  
            sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES (%s,%s,%s)' # Insertamos un registro
            valores = ('Alex', 'Roas', 'arojas@gmail.com') 
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona  SET nombre=%s, apellido=%s, email=%s WHERE ide_persona=%s' # Actualizamos el registro
            valores = (('Hector Luis', 'Huaquipa', 'luhuaquipa@gail.com',1),
                    ('Lucho', 'Benetes', 'lbenites@gmail.com',19)
                    )
            cursor.executemany(sentencia,valores) 
            

except Exception as e: # Captura la exception
    print(f'Ocurrio un erorr, se hizo un rollback: {e}')
finally:
    conexion.close()

print('Termina la transación')