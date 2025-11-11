# 1. Introduciion a las clases en Python
# Las calses son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos (atributos o propiedades) y funciones (metodos) en un solo lugar.

import os
os.system('cls')
#Ejemplo basico de una clase
class Coche:
  #atributo de calse (comparten todas las inatancias)
  tipo ='vehiculo de cuatro ruedas'

# metodo especial que es el el que construye el objeto
# se llama automaticamente este metodo cunado creas la instanica
  def __init__(self, marca, modelo, color):
  # atributos de la instancia
   self.marca = marca
   self.modelo = modelo
   self.color = color

  def arrancar(self):
   print(f'El coche {self.marca} {self.modelo} arranco! 🚗')

mi_coche = Coche('Toyota', 'Corolla','Rojo')
mi_coche.arrancar()

print(mi_coche.tipo)

coche_de_alonso =Coche('aston Martin','verde','verde')
coche_de_alonso.arrancar()
print(coche_de_alonso.marca)

#Encapsulacion: es ocultar los detalles internos de una clase y exponer solo la interfaz publica

#Crear una clase para llamar a la AI de OpenAI, DeepSeek O LO QUE SEA
import requests
class AI_API:
  def __init__(self,api_key,url, model):
    self.api_key = api_key
    self.url = url
    self.model = model
 
  def call(self,prompt):
    headers = {
      'Content-Type':'application/json',
      'Authorization': f'Bearer {self.api_key}'
    }
    data = {
      'model': self.model,
      'messages': [{'role':'user', 'content':prompt}]
    }
    response = requests.post(self.url, json=data, headers= headers)
    # Mostrar estado HTTP si algo falla
    if response.status_code != 200:
        print(f"⚠️ Error HTTP {response.status_code}")
        print("Respuesta del servidor:")
        print(response.text)  # Mostrar el contenido para depurar
        return

    res_json = response.json()

    # Verificar si 'choices' existe antes de acceder
    if 'choices' in res_json:
        print(res_json['choices'][0]['message']['content'])
    else:
        print("⚠️ Respuesta inesperada:")
        print(res_json)
    res_json = response.json()
    # print(res_json['choices'][0]['message']['content'])

print('\nOPEN_AI:')
# openai_api = AI_API(OPENAI_KEY, 'https://api.openai.com/v1/chat/completions','gpt-4o-mini')

openai_api.call('Escribe un breve poema sobre la programacion')


# print('\DEEPSEEK:')
# deepseek_api = AI_API(DEEPSEEK_KEY, 'https://api.deppseek.com/chat/completions' , 'deepseek-chat')

# deepseek_api.call('Escribe un breve poema sobre la programacion')
