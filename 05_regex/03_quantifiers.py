# 03 -Quantifiers
# Los quantifiers se utilizan para especificar cuantas ocurrencias de un caracter o grupo de caracteres se deben encontrar en una cadena

import os, re
os.system('cls')

# *: puede aparecer 0 o mas veces
texto = "aaaba"
patron = 'a*'
encontrado = re.findall(patron, texto)
print(encontrado)

# Ejercicio 1:
# Cuantas palabras tienen de 0 a mas "a" y despues una "b"?
#

#  # +: una a mas veces?
texto ='ddddd aaaa ccc a bb aa casa'
patron = 'a+'
encontrado = re.findall(patron, texto)
print(encontrado)

# ?: Cero o una vez
texto = 'aaabacb'
patron = 'a?b'
encontrado = re.findall(patron, texto)
print(encontrado)

# Ejeciricio : Haz opcional que aparezca un +34 en
#  el siguiente texto
telefono = '+34 654789987'
patron = r'( \+|00)?34 .\d{9}'

# {n}: Exactamente n veces
texto = 'aaaaaa  aa aaa'
patron = 'a{3}'
encontrado =  re.findall(patron, texto)
print(encontrado)

# {n, m}: De n a m veces
texto = 'u uu uuu u'
patron = r'\w{2,3}' 
encontrado = re.findall(patron, texto)
print(encontrado)

# EJERCICIO:
# Encuentra las palabras de 4 a 6 letras 
palabras = ' ala casa arbol, leon, cinco, muricelago'
patron = r'\b\w{4,6}\b'
encontrado = re.findall(patron,palabras)
print(encontrado)

# EJERCICIO:
# Encuentra las palabras de mas de seis letras
palabras = ' ala fantastico casa arbol, leon, cinco, murcielago'
patron = r'\b\w{6,}\b'
encontrado = re.findall(patron,palabras)
print(encontrado)