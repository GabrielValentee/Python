import requests
import json

OMDB_API_KEY = '23E45309'
BASE_URL = "https://www.omdbapi.com"

def search_title(title):

    params = {
        't': title,
        'apikey': OMDB_API_KEY
    }


    print(f"Buscando informações para: {title} ...")

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:

            data = response.json()

            if data.get('Response') == 'True':
                print("Titulo encontrado com sucesso")
                return data
            else:
                print(f"Erro ao buscar: {data.get [ 'Erro', 'Titulo não encontrado ou outro erro da API.']}")
                return None
        else:
            print(f"Erro na requisição HTTP. status code: {response.status_code}")
            print(f"Resposta da API: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de conexão: {e}")
        return None