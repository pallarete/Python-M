# 04 - Diccionarios
# Los dicccionarios son colecciones  de pares clave-valor
# Sirven para almacenar datos relacionados
import os
os.system('cls')
#  ejemplo tipico de diccionario
persona = {
  'nombre' : 'Alex',
  'edad': 45,
  'es_estudiante':True,
  'calificaciones': [7,8,9],
  'socials': { 
    'twitter':"Alexdev",
    "instagram": "Alexdev",
    "facebook":"alexdev"
  }
}

# Para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])
print('Cambiando valores')

# Cambiar valores al acceder
persona["nombre"] = "Santiago"
persona['calificaciones'][2]= 5

print(persona["nombre"])
print(persona['calificaciones'][2])
print(persona)

# Eliminar completamente una propiedad
del persona ["edad"]
print(persona)

# Para acceder a una propiedad eliminada
es_estudiante = persona.pop("es_estudiante")
print(f'es_estudiante: {es_estudiante}' )
print('Hola')
print(persona)

# Sobreescribir un dicccionario con otro diccionario
a = {'name':'midudev', "age":23}
b = {'name':'manolo', 'es_estudiante':True}
a.update(b)
print(a)

# comprobar si existe una propiedad
print('nombre' in persona)

# obtener todas las claves
print('\nKeys')
print(persona.keys())

# Obtener todos los valores
print('\nValores')
print(persona.values())

# Obtener claves y valores
print('\nItems:')
print(persona.items())