# 04 - Listas
# Secuencias mutables de elementos.Pueden conyener elementos
# de diferentes tipos
import os
os.system('cls')

lista1 = ['a','b','c','d','@']

#Añade un elemento al final de la lista
lista1.append('e')
print(lista1)

#Añade un elemento en la posicion que le indiquemos
# como primer parametro
lista1.insert(0, '@')
print(lista1)

#Agrega elementos al final de la lista.Extiende la lista
lista1.extend(['🚗','🍔'] )
print(lista1)

# Eliminar la primera aparicion de el termino indicado
lista1.remove('@')
print(lista1)

ultimo = lista1.pop()#Elimina el ultimo elemento de la lista.
print(ultimo)
print(lista1)

#Elimina el elmento del indice pasado
primera = lista1.pop(0)
print(primera)
print(lista1)

#Eliminar por lo bestia
del lista1[-1]
print(lista1)

#Eliminar un rango de elementos
lista2 = [0,1,2,3,4,5,6,7,8,9]
del lista2[1:5]
print(lista2)

#Borrar todo lo que hay en una lista
lista1.clear()
print(lista1)


#Mas metodos utiles
print('Ordenar listas modificando la original')
numeros = [90,56,4,23,11,]
numeros.sort()
print(numeros)

print('Ordenar listas creando una nueva lista')
numeros = [90,56,4,23,11,]
ordenados_numeros = sorted(numeros)
print(ordenados_numeros)

print('Ordenar una lista de cadenas de texto(todo minuscula)')
frutas = ['manzana','pera','limon','manzana','pera','limon']
frutas_ordenadas = sorted(frutas)
print(frutas_ordenadas)

print('Ordenar una lista de cadenas de texto(mayus i minus)')
frutas = ['manzana','Pera','Limon','manzana','pera','limon']
frutas.sort(key=str.lower)
print(frutas)

# Mas metodos utiles
animals = ['🤢','📺','➡️','✅','🤢']
print(len(animals))# Tamaño de las listas->5
print(animals.count('🤢'))# Cuantas veces aparece el elemento '🤢'->2
print('🏐'in animals) # Comprueba si hay algo en la lista. Valor Booleano
print('🏐'not in animals) # Comprueba si hay algo en la lista. Valor Booleano

###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
















