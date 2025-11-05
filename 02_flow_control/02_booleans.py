# 02 - Booleanos
# Valores logicos: True (Verdadero) y False (falso)
# Fundamentos para el control de flujo y la logica en programacion
import os
os.system('cls')
# Los booleanos representan valores de verdad: True y False
print('\nValores booleanos basicos:')
print(True)
print(False)

#Operadores de comparacion: devuelven un valor booleano
print('\nOperadires de comparacion:')
print('5  >  3:',  5  > 3  ) # True
print('5  <  3:',  5  < 3  ) # False
print('5 ==  5:',  5 == 5  ) # True (igualdad)
print('5 !=  3:',  5 != 3  ) # True (desigualdad)
print('5 >=  5:',  5 >= 5  ) # True (mayor o igual que)
print('5 <=  3:',  5 <= 3  ) # False (menor o igual que)

print('\nComparacion de cadenas')
print('manzana < pera:', 'manzana' < 'pera') # True
print( "'Hola' == 'hola'","Hola"== "hola")

#Operaadores lógicos: and, or, not
print("\nOperadores lógicos" )
print("True and True:  ",  True and True ) # True
print("True and False: ", True and False ) # False
print("True or False:  ",  True or False ) # True
print("False or False: ", False or False ) # False
print("not True:       ",   not True )     # False
print("not False:      ",  not False )     # True

#Tablas de la verdad
print('\nTablas de la verdad')
print('\nand:')
print('True and False', True and False )
print('True and True',  True and True )
print('False and True', False and True )
print('False and False',False and False )


print('\n or:', )
print('True or True ',    True or True)
print('True or False',   True or False)
print('False or True',   False or True )
print('False or False ', False or False)

