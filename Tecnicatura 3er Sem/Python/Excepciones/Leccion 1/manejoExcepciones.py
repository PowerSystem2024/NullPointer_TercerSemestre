from NumerosIgualesException import NumerosIgualesException


try:
    a= int(input('Digite el primer número: '))
    b= int(input('Digite el segundo número: '))
    if a == b:
        raise NumerosIgualesException('son números  iguales')
    resultado = a/b # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {type(e)}') # EXCEPTION SPECIFIC
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error: {type(e)}')# podemos usar la clase padre de Exception lo mas generico, pero si queremos captura algo mas 
except Exception as e:
    print(f'Exception - Ocurrio un error: {type(e)}') # EXCEPTION GENERAL
else:
    print('NO  se arrojo ninguna Excepción ')
finally:  # siempre se va a ejecutar
    print('Ejecución de este bloque finally')

print(f'El resultado es : {resultado}')
print('seguimos...')

