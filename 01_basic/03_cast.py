# 03 - casting de types
# Transformar un tipo de valor a otro 
import os
os.system('cls')

print('Conversion de tipos')
print(type('100'))
print(type(int('100')))
print("\n")
print(2 + int('100'))
print(str(2) + '100')
print("\n")
print(type(float('3.1416')))
print("\n")
print(bool(3))
print(bool(0))
print(bool(-1))
print("\n")
print(bool(""))
print(bool(" "))
print(bool("False"))
#Este casting solo quita la parte decimal da igual el valor despues de la coma
print(int(3.5))
# Este casting redondea al par mas cercano
print(round(3.5))
print(round(2.5))
# Este round redondea al enteromas cercano
print(round(2.51))
print(round(2.49))

