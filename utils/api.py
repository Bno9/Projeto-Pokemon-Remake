import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon(nome_ou_id):

    url = f"{BASE_URL}/pokemon/{nome_ou_id}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Pokémon {nome_ou_id} não encontrado.")
    
    print("pokemon criado com sucesso")

    return response.json()