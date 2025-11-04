# 04 - variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinamico y de tipado fuerte

# Asignar una variable:
my_name = 'alexdev'
print(my_name)

age= 45
print(age)

age = 41
print(age)
# Tipado dinamico: el tipo de dato se determina en tiempo de ejecucion
# no hay que declararlo explicitamente
name = 'Alexdev'
print(type(name))
name = 32
print(type(name))

# Tipado fuerte: Python no realiza conversiones de tipo automaticamente
# print(10 + '2')

# f-string (literal de cadena de formato)
print(f'Hola {my_name}, tengo {age} años')
print(f'Hola {my_name}, tengo {age + 5} años')

# No recomendada forma de asignar variables
name, age, city = "alexdev",43,'Bogota'

# Convenciones de nombres de variables
mi_nombre_de_variable = 'ok'
nombre = 'ok'

# Para las constantes (que no hay) 
MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes

# Ejemplo de data anotations
is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 42
print(is_user_logged_in)

