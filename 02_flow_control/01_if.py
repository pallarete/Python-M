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