import requests
from datetime import datetime, time

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokeapi(nome_ou_id, endpoint):
    """
    Função que retorna um pokemon, item ou ataque, dependendo do endpoint passado
    
    Args:
        nome_ou_id (str|int): Nome ou id que deseja buscar da api 
        endpoint (str): Endpoint da api que vai ser acessada

    Returns:
        dict: Json da pokeapi
    """

    url = f"{BASE_URL}/{endpoint}/{nome_ou_id}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"{endpoint} {nome_ou_id} não encontrado.")
    
    # print(f"{endpoint} transferido da api com sucesso")

    return response.json()


def get_all_generation(geracao):
    """
    Função que retorna toda a geração 1 de pokemons da pokeapi
    (pode retornar qualquer outra, basta mudar o final do endpoint)
    
    Args:
        None

    Returns:
        dict: Json da pokeapi
    """

    url = f"{BASE_URL}/generation/{geracao}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"geração não encontrada.")
    
    generation = response.json()

    inicio = datetime.now()

    for j in generation["pokemon_species"]:
        final = datetime.now()
        tempo = final - inicio
        print(f"{j["name"]} transferido da api com sucesso às {datetime.now()} Tempo de espera: {tempo}")

    print("Geração transferida com sucesso.")
    return response.json()



def get_move_stats(url_move):

    url = f"{url_move}"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"ataques não encontrados.")
    
    moves_stats = response.json()

    inicio = datetime.now()
    final = datetime.now()
    tempo = final - inicio
    print(f"{moves_stats["name"]} transferido da api com sucesso às {datetime.now()} Tempo de espera: {tempo}")
    
    return response.json()

def get_pokeapi_move():
    """
    Função que retorna um pokemon, item ou ataque, dependendo do endpoint passado
    
    Args:
        nome_ou_id (str|int): Nome ou id que deseja buscar da api 
        endpoint (str): Endpoint da api que vai ser acessada

    Returns:
        dict: Json da pokeapi
    """

    url = f"{BASE_URL}/move?limit=1000"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"não encontrado.")

    return response.json()