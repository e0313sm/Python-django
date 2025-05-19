import requests
import json

url = "https://api-colombia.com/api/v1/Department"

try:
    respuesta = requests.get(url, timeout=18)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        for departamento in datos:
            id = departamento.get('id', 'Nombre no disponible')
            nombre = departamento.get('name', 'Nombre no disponible')
            poblacion = departamento.get('population', 'Poblacion no disponible')
            print(f"Id:{id} | Nombre: {nombre} | Población: {poblacion}")

    else:
        print(f"Error en la solicitud: Código {respuesta.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Error de conexión: {error}")