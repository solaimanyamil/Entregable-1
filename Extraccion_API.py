# -*- coding: utf-8 -*-
"""
@author: Yamil
"""
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

