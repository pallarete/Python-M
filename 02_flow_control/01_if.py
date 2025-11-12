# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de codigo solo si se cumplen ciertas condiciones
import os
os.system('cls')
print('\n Sentencia simple condicional')

edad = 18
if edad >= 18:
  print('Eres mayor de edad')
  print('Felicidades')

edad = 15
if edad >= 18:
  print('Eres mayor de edad')
  print('Felicidades')

print('\nSentencia condicional con else')
edad = 15
if edad >= 18:
  print('Eres mayor de edad')
else:
  print('Eres menor de edad')

print('\nSentencia condicional con elif')
nota = 7
if nota >= 9:
  print('Sobresaliente')
elif nota >= 7:
  print('Notable')
elif nota >=5:
  print('Aprobado')
else:
  print('No esta calificado')

print('\nCondiciones multiples')
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
  print('Puedes conducir 🚗')
else:
  print('POLICIA!!!!!! 🚓')

#   un pueblo de isla margarita
if edad >= 18 or tiene_carnet:
  print('Puedes conducir')
else:
  print('Paga al policia y te deja conducir')

es_fin_de_semana= False
if not es_fin_de_semana:
  print('Alex! hay que estrimear')

print('\nAnidar condicionales')
edad = 14
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print('Puedes ir a la discoteca')
  else:
    print('Quedate en casa')
else:
  print('No puedes entrar a la disco')

# Lo mismo con mas operadores pero al ser mas restrictivo tiene menos anidacion
if edad < 18:
  print('No puedes entrar a la disco')
elif tiene_dinero:
  print('Puedes ir a la disco')
else:
  print('Quedate en casa')

numero = 5
if numero: #True
  print('El numero no es cero')

numero = 0
if numero:
  print('Aqui no entrara nunca')

nombre = 'Juan'
if nombre:
  print('El nombre no es vacio')

numero = 3 #asignacion
es_el_tres = numero == 3 # comparacion
if es_el_tres:
  print('El numero es 3')

print('\nLa condicion ternaria')
# es una forma concisa de un if-else en un linea de codigo
# [codigo si cumple la condicion] if [condicion]else[codigo si no cumple]
edad = 17
mensaje= 'Es mayor de edad' if edad>= 18 else 'Es menor de edad'
print(mensaje)
print( 'Es mayor de edad' if edad>= 18 else 'Es menor de edad')

print('EJERCICIOS')
###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
numero1 = input(f'Introduce un numero:')
numero2 = input(f'Introduce otro numero:')

if numero1 == numero2:
  print(f'El numero {numero1} es igual al numero : {numero2}')
elif numero1 > numero2:
  print(f'El numero {numero1} es mayor que el numero {numero2}')
else:
  print(f'El numero {numero2} es mayor que el numero {numero1}')


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)


numero1 = int(input('Introduce un numero:'))
numero2 = int(input('Introduce otro numero:'))
operacion = input(f'Que operacion quieres hacer con esos numeros?:')

if operacion == '+':
  print(f'El resultado es:  {numero1 + numero2}' )

elif  operacion == '-':
  print(f'El resultado es:  {numero1 - numero2}' )

elif operacion == '*':
  print(f'El resultado es:  {numero1 * numero2}' )

elif operacion == '-':
  if numero2 !=0:
   
    print(f'El resultado es:  {numero1 / numero2}' )
  
  else:
  
    print(f'No se puede dividir entre cero' )

else:
    print('Operacion no valida}' )

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
year = int(input('Introduce un año:'))
if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
  print(f'El año {year} es bisiesto ')
else: print(f'El año {year} no es bisiesto ') 

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
edad = int(input('Introduce tu edad:'))
if edad >= 0 and edad <= 2:
  print('Eres un bebe')

elif edad >=3 and edad <= 12:
  print('Eres un niño')

elif edad >= 13 and edad <= 17:
  print('Eres un Adolescente')

elif edad >= 18 and edad <= 64:
  print('Eres un Adulto')

else:
  print('Eres un Senior')




