# 04 - Funciones
# Bloques de codigo reutilizable y parametrizables
# para hacer tareas especificas
import os
os.system('cls')

'''
Definicion de una funcion:
def nombre_de_la_funcion(parametro1, parametro2,...)
 # docstring
 # cuerpo de la funcion
 return valor_de_la_funcion # opcional
'''

#ejemplo d euna funcion para imprimir en consola
def saludar():
  print('Hola')

# Ejemplo de una funcion con parametros
def saludar_a(nombre):
  print(f'Hola {nombre}!')

saludar_a("Alex")
saludar_a("Arantxa")
saludar_a("Prince")

# Parametro es lo que acepta la funcion
# El argumento es lo que se la pasa a la funcion

# Funcion con mas parametros
def sumar (a,b):
  suma = a + b
  return suma

result =sumar(2,3)
print(result)

# Documentar las funciones con docstring
def restar(a,b):
  '''Resta dos numeros y devuelve el resultado'''
  return a -b

print(restar.__doc__)

help(restar)

#Parametros por defecto
def multiplicar (a , b = 2):
  return a * b

print(multiplicar(2))

#Argumento por posicion
def describir_persona(nombre,edad,sexo):
  print(f'Soy {nombre}, tengo {edad} y me identifico como {sexo}')

#parametros son  posicionales
describir_persona('Alex',34,'marrajo')

#Argumentos por clave
# Parametros nombrados
describir_persona(sexo='gato',nombre ='alexdev',edad=34)

#Argumentos de longitud variable(*args)

def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma+= numero
  return suma

print(sumar_numeros(1,2,3,4,5))
print(sumar_numeros(6,9))
print(sumar_numeros(1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2))

# Argumentos de calve-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f'{clave}:{valor}')

mostrar_informacion_de(nombre = 'AlexDev', edad = 45, sexo = 'marrajo')
print('')
mostrar_informacion_de(nombre = 'Arantxa', edad = 34, sexo = 'poco', hijos = 'si')
print('')
mostrar_informacion_de(nombre = 'Louis', edad = 18, sexo = 'el que le dejan', pesadete = 'si')

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora