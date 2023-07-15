# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 16:41:53 2023

@author: Yamil
"""
'''
import requests
import json

# URL de la API
url = 'https://nba-stats-db.herokuapp.com/api/playerdata/topscorers/playoffs/2023/'

# Realizar la solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Extraer los datos en formato JSON
    data = response.json()
    
    # Imprimir los datos con indentación de 4 espacios
    print(json.dumps(data, indent=4))
else:
    # Manejar el caso de error
    print('Error al realizar la solicitud:', response.status_code)
'''

#%%


import requests
import json

# Hacer la solicitud a la API:
response = requests.get('https://nba-stats-db.herokuapp.com/api/playerdata/topscorers/playoffs/2023/')

# Verificar si la solicitud fue exitosa (código de estado 200):
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()

    # Leer los datos en un diccionario:
    dictionary_data = dict(data)
    print(dictionary_data)
else:
    # Si la solicitud no fue exitosa, mostrar el código de estado:
    print("Error en la solicitud. Código de estado:", response.status_code)

