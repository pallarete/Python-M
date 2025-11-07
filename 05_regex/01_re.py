#
# 01 - Expresiones regulares
# Las Regex son una secuencia de caracteres que forman un patron de busqueda
# Se utilizan para la busqueda de cadenas de texto, validacion de datos,etc
# Porque aprender Regex? pusqueda avanzada: Encontrar patrones especificos en textos 
# grandes de forma rapida y precisa. (un editor de texto solo usando Regex)
#-Validacion de datos: Asegurarte que los datos que ingresa un usuario como el elmail,
# telefono, etc. son correctos
# Extraccion de informacion permitir obtener y aprovechar datos especificos de un texto
# como nombres, fechas o direcciones
# Manipulacion del texto: Extraer, reemplazar y modificar partes de la cadena de texto facilmente
import os
os.system('cls')
# 1.importar el modulo de python para manejar RE
import re
# 2. Crear un patron
pattern = 'Hola'
# 3. El texto donde queremos buscar
text = 'Hola mundo'
# 4. Usar la funcion de busqueda de "re"
result = re.search(pattern, text)

if result:
  print('He encontrado el patron en el texto')
else:
   print('No he encontrado el patron en el texto')

# .group() devuelve la cadena que coincide con el patron
print(result.group())

# .start()devolver la posicion inicial de la coincidencia
print(result.start())

# .end()devolver la posicion final de la coincidencia
print(result.end())

# EJERCICIO 01
#  Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posicion empieza y en que posicion acaba la coincidencia
text = 'Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta' \
'ver como la puede cagar con los Regex para ir con cuidado'
pattern = 'IA'
result = re.search(pattern, text)
if result:
  print(f'He encontrado el patron en el texto en la posicion {result.start()} y termina en la posicion {result.end()}')
else:
  print('No se ha encontrado nada')

# Encontrar todas las coincidencias de un patron
text = 'Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil, ojo con Python'
pattern = 'Python'

matches = re.findall(pattern, text)
print(len(matches))

#iter() devuelve un iterador que contiene todos los resultados de la busqueda
text = 'Me gusta Python. Python es lo maximo. Aunque Python no es tan dificil, ojo con Python'
pattern = 'Python'
# finditer nos devuelve un grupo de coincidencias iterables
matches = re.finditer(pattern, text)

for match in matches:
  print(  f'{match.group()}, { match.start()},{match.end()} ' )

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en
# el siguiente texto e indica en que posicion empieza y
# termina cada coincidencia y cunatas veces se encontro
text = 'Este es el curso de Python de midudev. Suscribete a midudev si te gusta este contenido! midu'

pattern = 'midu'

# Modificadores
# Los modificadores son opciones que se pueden agregar a un patron
# para cambiar su comportamiento

# re.IGNORECASE(): Ingnora las mayusculas y minusculas

text = 'Todo el mundo dice que la IA nos va a quitar el trabajo. Pero' \
'la ia no es tan mala. Viva la Ia!'
pattern = 'IA'
result = re.findall(pattern, text,re.IGNORECASE)
if result:
  print(result)

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el
# siguinete texto, sin distinguir entre mayuculas y minusculas
text = "Este es el curso de Python de midudev. !Suscribete a python" \
"si te gusta este contenido! PYTHON "

# Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patron en un texto

text = 'Hola, mundo! Hola de nuevo.'
pattern = 'Hola'
replacement = 'Adios'

new_text = re.sub(pattern, replacement,text)
print(new_text)
