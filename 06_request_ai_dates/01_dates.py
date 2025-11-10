# Trabajando con fechas y horas en Python

import os
os.system('cls')
from datetime import datetime, timedelta

# Obtener la fecha y hora actuales
ahora=datetime.now()
print(f'Fecha y hora actuales:  {ahora}')

# Crear una fecha y hora especificas
fecha_especifica = datetime(2021,2,1, 15, 00, 45)
print(f'Fecha y hora especificas {fecha_especifica}')

#Formatear fechas
# Metodo strftime() para formatear fechas
# Pasarle el objeto datetime y el formato especificada
# Formato: 
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
fecha_formateada = ahora.strftime('%A %B %Y %H:%M:%S')
print(f'Fecha formateada: {fecha_formateada}')

# Operaciones con fechas (sumar/restar dias, minutos, horas meses)
ayer = datetime.now() - timedelta(days=1)
print(f'Ayer: {ayer}')

mañana = datetime.now() + timedelta(days =1)
print(f'Mañana: {mañana}')

una_hora = datetime.now() + timedelta(hours = 1)
print(f'Una hora mas : {una_hora}' )

# Obtener componentes individuales de una fecha
year = ahora.year
print(year)

month = ahora.month
print(month)

#Calcular la diferencia entre dos fechas
date1 = datetime.now()
date2 = datetime(2025 ,5, 20, 16, 15, 0)
diferencia = date2 - date1

print( f'Diferencia entre las fechas : {diferencia}')

#Fechas en otro idioma





