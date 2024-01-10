import requests

def get_data():
    try:
        url = 'http://127.0.0.1:8000/tecsu/products/'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error al obtener productos: {err}")
        return None