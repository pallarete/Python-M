# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos 
# en las expresiones regulares

import os, re
os.system('cls')

# 1. El punto(.)
# Coincidir con cualquier caracter excepto una nueva linea
text = 'Hola mundo, H0la de nuevo, H$la otra vez'
pattern = 'H.la' #Cualquier hola mal escrito

found = re.findall(pattern, text)
print(found)

if found:
  print(found)
else:
  print('No se ha encontyrado el patron')

text = 'casa caasa cosa cisa cesa causa'
pattern = 'c.sa'
matches = re.findall(pattern, text)
print(matches)

#---------------------------
text = 'Hola mundo, H0la de nuevo, H$la otra vez'
pattern = r'H.la' #Cualquier hola mal escrito

found = re.findall(pattern, text)

if found:
  print(found)
else:
  print('No se ha encontyrado el patron')

 # Como usar la barra invertida para anular el 
 # significado especial de un simbolo 
text = 'Mi casa es blanca. Y el coche es negro.'

pattern = r'\.'

matches = re.findall(pattern, text)

print(matches)

# \d: coincide con cualquier digito (0-9)
text = 'El numero de telefono es 123456789'
# Me imprimes todos los numeros que encuentres
found = re.findall( r'\d', text)
print(found)

# Me imprimes patrones de tres numeros que encuentres
found = re.findall( r'\d\d\d', text)
print(found)

# Me imprimes un patron que ocurra 9 veces
found = re.findall( r'\d{9}', text)

print(found)

# EJERCICIO:  Detectar si hay un numero de España en el texto
# gracias al prefijo +34

texto = 'Mi numero de telefono es +34 654112233, anotalo vale?'
pattern = r'\+34 \d{9}'
found = re.search(pattern, texto)
if found:
  print(f'El numero de telefono es:{found.group()}')
else:
  print('No encontre el numero')
print(repr(texto))

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9)
texto = 'el_rubios_69'
pattern = r'\w'
found= re.findall(pattern, texto)
print(found)

# \s: Coincide con cualquier espcaio en blanco (espacio, tabulacion, salto de linea)
text = 'Hola mundo \n Como estas?\t'
pattern = r'\s'
found = re.findall(pattern, text)
print(found)

# ^: Coincide con el principio de una cadena
username = '423_name'
pattern = r'^\w' # validar nombre de usuario

valid = re.search(pattern, username)

if valid:
  print('El nombre de usuario es valido')
else:
  print('El nombre de usuario no es valido')

phone ='+123123123 654789999'
# Cuidado con los espacios en las REGEX!!!!
pattern = r'^\+\d{1,3} '
valid = re.search(pattern, phone)
if valid: print('\nEl numero de telefono es valido')
else: print('\nEl numero de telefono no es valido')

# $: Coincide con el final de una cadena
text = ' Hola Mundo'

pattern = r'mundo$'

valid= re.search(pattern , text)
if valid: print('Se encontro la coincidencia')
else: print('No se encnontro la coincidencia')

# EJERCICIO 
# Valida que un correo sea de gmail
texto = 'aranzazu@gmail.com'
patron = r'@gmail.com$'

valido = re.search(patron, texto)

if valido: print('El correo es gmail valido')
else: print('El email no es valido')

# EJERCICIO
# Tenemos una lista de archivos, necesitamos saber los nombres
#  de los ficheros con extension .txt
archivos ='file1.txt file2.pdf alex-of.webp secret.txt'

# \b: Coincide con el principio o final de una palabra
texto = 'casa casado casada, cosa, cosas, casa'
# asi no en base a este ejemplo
patron = r'casa'
encontrado = re.findall(patron, texto)
print(encontrado)

# Asi si que encotraremos la coincidencia lexica exacta por palabra
patron = r'\bc.sa\b'
encontrado = re.findall(patron, texto)
print(encontrado)

# |: Coincidir con una opcion u otra
frutas = 'platano , manzana, aguacate, pera, palta,aguacate,aguacate'
patron = r'aguacate|pera|p..a|\b\w{7}\b'
encontrados = re.findall(patron, frutas)
print(encontrados) if encontrados else print('No se encontro nada')