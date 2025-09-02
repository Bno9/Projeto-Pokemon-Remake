import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokeapi(nome_ou_id, endpoint):

    url = f"{BASE_URL}/{endpoint}/{nome_ou_id}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"{endpoint} {nome_ou_id} não encontrado.")
    
    print(f"{endpoint} transferido da api com sucesso")

    return response.json()