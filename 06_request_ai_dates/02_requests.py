# Como hacer peticiones a APIs con Python
# Con y sin dependencias

import os
os.system('cls')

# 1. Sin dependencias (dificil y sin dependencias)
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts/"
try:
  response = urllib.request.urlopen(api_posts)
  data = response.read()
  json_data = json.loads(data.decode('utf-8'))
  # print(json_data)
  # response.close()
except urllib.error.URLError as e:
  print(f'Error en la solicitud {e}') 

# 2. Con dependencia (requests)
import requests

print('\nGET: ')
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
json=response.json()
print(json[0])

# 3. Un POST
api_posts = "https://jsonplaceholder.typicode.com/posts/"
print('\nPOST: ')
try:  
  input = {
    'title':'alex',
    'body':'dev',
    'userId': 5
  }
  response = requests.post(api_posts, json=input)
  print(response.json())
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f'Error en la solicitud: {e}')

# 3. Un PUT
api_posts = "https://jsonplaceholder.typicode.com/posts/1"
print('\nPUT: ')
try:  
  input = {
    'title':'fafoti',
    'body':'gil',
    'userId': 1,
    'id':1
  }
  response = requests.put(api_posts, json=input)
  print(response.json())
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f'Error en la solicitud: {e}')


# 4. OTRO PATCH
api_posts = "https://jsonplaceholder.typicode.com/posts/5"
print('\nPUT: ')
try:  
  input = {
    'title':'AlexGuapoi',
    'body':'Sandra Puta pero que muy puta',
    'userId': 1,
    'id':5
  }
  response = requests.patch(api_posts, json=input)
  print(response.json())
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f'Error en la solicitud: {e}')


#Usar la API de GPT-4o o de OpenAI