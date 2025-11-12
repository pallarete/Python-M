import requests
import os
os.system('cls')

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air'
response = requests.get(url)
print(response.status_code)
print(response.text)