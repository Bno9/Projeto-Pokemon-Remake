import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from classes.Pokemons import Pokemon
from utils.api import get_pokemon

lista_pokemon = []


try:
    with open("pokemons.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

        for item, valor in dados.items():
            Poke_formatado = Pokemon(item, valor["tipos"], valor["stats"])
            lista_pokemon.append(Poke_formatado)
except json.JSONDecodeError:
    lista_pokemon = []


def criar_pokemon():
        nome = input("Digite o nome do pokemon: ")

        pokemon_json = get_pokemon(nome)

        for i in lista_pokemon:
             if pokemon_json["name"] == i.nome:
                print(f"{pokemon_json["name"]} ja existe")
                return

        stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_json["stats"]}
        tipos = [tipo['type']['name'] for tipo in pokemon_json['types']]

        Poke = Pokemon(pokemon_json["name"], tipos, stats)
        lista_pokemon.append(Poke)

criar_pokemon()

with open("pokemons.json", "w", encoding="utf-8") as arquivo:
    json_formatado = {}

    for poke in lista_pokemon:
        json_formatado[poke.nome] = {"tipos": poke.tipos,
                                    "stats": poke.stats}
     
    json.dump(json_formatado, arquivo, indent=4)


