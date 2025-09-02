import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from classes.Pokemons import Pokemon
from classes.Itens import Item
from utils.api import get_pokeapi

lista_pokemons = []
lista_itens = []


try:
    with open("pokemons.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

        for item, valor in dados.items():
            Poke_formatado = Pokemon(item, valor["tipos"], valor["stats"])
            lista_pokemons.append(Poke_formatado)
except json.JSONDecodeError:
    lista_pokemon = []





def pedir_input(endpoint):
    return input(f"Digite o nome do {endpoint}: ")
 

def criar_pokemon(endpoint):
    nome = pedir_input(endpoint)

    for i in lista_pokemons:
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

    Poke = Pokemon(pokemon_json["name"], tipos, stats)
    lista_pokemons.append(Poke)

def criar_item(endpoint):
    nome = pedir_input(endpoint)

    item_json = get_pokeapi(nome, endpoint)

    for item in lista_itens:
        if item_json["name"] == item.nome:
            print(f"{item_json["name"]} ja existe")
            return
        
    itens = Item(item_json["name"], item_json["cost"], item_json["category"]["name"], [item["name"] for item in item_json["attributes"]])
    lista_itens.append(itens)

def criacao():
    end_map = {"pokemon": criar_pokemon,
           "item": criar_item}
    

    while True:
        for i in lista_itens:
            print(i.nome)

        for i in lista_pokemons:
            print(i.nome)

        endpoint = input("Digite qual requisição deseja fazer (pokemon, item. 0 pra sair):  ")

        if endpoint == "0":
            return

        escolha = end_map.get(endpoint, lambda: print("Opção inválida"))

        escolha(endpoint)


criacao()

with open("pokemons.json", "w", encoding="utf-8") as arquivo:
    json_formatado = {}

    for poke in lista_pokemons:
        json_formatado[poke.nome] = {"tipos": poke.tipos,
                                    "stats": poke.stats}
     
    json.dump(json_formatado, arquivo, indent=4)

