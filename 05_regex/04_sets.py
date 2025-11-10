import re, os
os.system('cls')
#[: Coincide con cualquier caracter] dentro de los corchetes
username ='rub.$ius_69+'
patron = r'^[\w._%+-]+$'

encontrado = re.search(patron, username)

if encontrado:
  print('El nombre de ususario es valido: ', encontrado.group())
else:
  print('El nombre de usario no es valido')

# Buscar todas las vocales de una palabra
texto = 'Hola Mundo'
patron = r'[aeiou]'
encontrado =re.findall(patron, texto)
print(encontrado)

# Una regex para encontrar las palabras man, fan y ban
# pero ignora el resto
texto = 'man ran fan ñam ban'
patron = r'[mfb]an'
encontrado = re.findall(patron, texto)
print(encontrado)

# EJERCICIO
# Nos han complicado un poco el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras
# Solo queremos las palabras man, fan y ban
texto = 'ominam fanatico man bandana'
patron = r'[mfb]an'
# \b:

# Encontrar un patron de numeros
texto = '22'
patron = r'[4-9]'
encontrado = re.findall(patron, texto)
print(encontrado)

#Ejercicio final con todo lo aprendido.
# Mejorar esto: https://www.computerhope.com//jargon/r/
# regular-expression.png

# Buscar corner cases que no pasa y arreglarlo

# Coincidencias negadas
# [^]: Coincide  con cualquier caracter que no este dentro de los corchetes
texto =' Hola Mundo'
patron = r'[^aeiou]'
encontrado = re.findall(patron, texto)
print(encontrado)






























