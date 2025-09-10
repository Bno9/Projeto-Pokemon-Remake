import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from classes.Pokemons import Pokemon
from classes.Itens import Item 
from utils.api import get_pokeapi, get_all_generation

class GameData:
    def __init__(self):
        self.lista_pokemon = self.carregar("pokemon.json", Pokemon, ["tipos", "stats"])
        self.lista_items = self.carregar("itens.json", Item, ["custo", "categoria", "atributos"])
        self.pokedex = {}
        self.mochila = self.carregar("mochila.json", dict, [])
        self.dinheiro = 10000
        self.estoque = []

    @staticmethod
    def carregar(file: str, classe, campos):
        lista = []
        dicionario = {}

        try:
            with open(file, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

                for item, valor in dados.items():
                    if classe == dict:
                        dicionario[item] = valor

                    else:
                        args = [item] + [valor[campo] for campo in campos]
                        lista.append(classe(*args))


        except (json.JSONDecodeError, FileNotFoundError):
            pass

        return dicionario if classe == dict else lista

    @staticmethod
    def salvar(lista, file: str, mapa_conversao):
        with open(file, "w", encoding="utf-8") as arquivo:
            dados = {obj.nome: mapa_conversao(obj) for obj in lista} if isinstance(lista, list) else lista
            json.dump(dados, arquivo, indent=4)    

def pedir_input(endpoint: str) -> str:
    return input(f"Digite o nome do {endpoint}: ")
 
def criar_pokemon(endpoint: str):
    """
    Função que cria um pokemon atraves do nome ou id passado pelo usuario
    
    Args:
        None

    Returns:
        None
    """

    nome = pedir_input(endpoint)

    for i in gamedata.lista_pokemon:
        if nome == i:
            print(f"{i} ja existe")
            return

    pokemon_json = get_pokeapi(nome, endpoint)

    # for i in lista_pokemons:
    #     if pokemon_json["name"] == i.nome:
    #         print(f"{pokemon_json["name"]} ja existe")
    #         return

    stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_json["stats"]}
    tipos = [tipo['type']['name'] for tipo in pokemon_json['types']]

    stats["xp"] = 0

    Poke = Pokemon(pokemon_json["name"], tipos, stats)
    gamedata.lista_pokemon.append(Poke)

    gamedata.salvar_json(GameData.lista_pokemon, "pokemons.json", poke_dict)

def criar_geracao():  #apenas um teste porque ainda nao tenho certeza de como quero fazer a criação dos pokemons, mas por enquanto vou trabalhar apenas com a primeira geração
    """
    Função que cria todos os pokemons da primeira geração (pode ser alterado para qualquer geração,
    basta ir na api.py e mudar o endpoint do get_all_generation)
    e guarda em uma lista (lista_pokemons)
    
    Args:
        None

    Returns:
        None
    """
    geracao1 = get_all_generation()


    for i in geracao1["pokemon_species"]:
        pokemon_json = get_pokeapi(i["name"], "pokemon")

        stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_json["stats"]}
        tipos = [tipo['type']['name'] for tipo in pokemon_json['types']]

        Poke = Pokemon(pokemon_json["name"], tipos, stats)
        gamedata.lista_pokemon.append(Poke)

        gamedata.salvar(gamedata.lista_pokemon, "pokemons.json", poke_dict)

def criar_item(endpoint: str):
    """
    Função que cria um item atraves do nome ou id passado pelo usuario
    
    Args:
        None

    Returns:
        dict: Json da pokeapiNone
    """

    nome = pedir_input(endpoint)

    item_json = get_pokeapi(nome, endpoint)

    for item in gamedata.lista_items:
        if item_json["name"] == item.nome:
            print(f"{item_json["name"]} ja existe")
            return
        
    itens = Item(item_json["name"], item_json["cost"], item_json["category"]["name"], [item["name"] for item in item_json["attributes"]])
    gamedata.lista_items.append(itens)

    gamedata.salvar(gamedata.lista_items, "itens.json", item_dict)

def criacao():
    """
    Função que recebe o endpoint escolhido pelo usuario,
    verifica se existe a opção, assimila a chave do dicionario com o valor,
    e envia o endpoint para função respectiva
    
    Args:
        None

    Returns:
        None
    """

    end_map = {"pokemon": criar_pokemon,
           "item": criar_item}
    

    while True:
        endpoint = input("Digite qual endpoint deseja acessar (pokemon, item. 0 pra sair):  ")

        if endpoint == "0":
            return

        escolha = end_map.get(endpoint, lambda: print("Opção inválida"))

        escolha(endpoint)

def poke_dict(obj) -> dict:
    return{
        "tipos": obj.tipos,
        "stats": obj.stats
    }

def item_dict(obj) -> dict:
    return{
        "custo": obj.custo,
        "categoria": obj.categoria,
        "atributos": obj.atributos
    }


gamedata = GameData()