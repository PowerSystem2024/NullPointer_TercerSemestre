import logging as log 


#Llamamos una configuración básica de logging
log.basicConfig(level=log.DEBUG, #Nivel del log
                format= '%(asctime)s:%(levelname)s [%(filename)s: %(lineno)s] %(message)s', #Formato del mensaje
                datefmt='%I:%M:%S %p', #Formato de la fecha
                #Archivo donde se guardan los logs
                handlers=[ 
                    log.FileHandler('capa_datos.log'), 
                    log.StreamHandler( ), 
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivle debug')
    log.info('Mensje de nivel info')
    log.warning('Mensaje de nivel warning')
    log.error('Mensaje de nivel error')
    log.critical('Mensaje de nivel critical')
