import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from classes.Pokemons import Pokemon
from classes.Itens import Item, Pokebola
from classes.Ataques import Ataques
from utils.api import get_pokeapi, get_all_generation, get_move_stats, get_pokeapi_move

class GameData:
    """Classe com todas informações do jogo"""
    def __init__(self):
        self.lista_pokemon = self.carregar("pokemons.json", Pokemon, ["tipos", "stats", "lista_ataques"])
        self.lista_items = self.carregar("itens.json", Item, ["custo", "categoria", "atributos", "quantidade"])
        self.lista_ataques = self.carregar("ataques.json", Ataques, ["dano", "precisao", "tipo"])
        self.pokedex = self.carregar("pokedex.json", Pokemon, ["tipos", "stats"])
        self.mochila = self.carregar("mochila.json", Item, ["custo", "categoria", "atributos", "quantidade"])
        self.dinheiro = 1000000
        self.estoque = []

    def get_ataque(self, nome_ataque):
        for ataque in self.lista_ataques:
            if ataque.nome == nome_ataque:
                return ataque
            return None

    @staticmethod
    def carregar(file: str, classe, campos):
        """Menu de carregamento dos json
    
          Args: file: o arquivo que vai ser aberto 
                classe: a classe que será utilizada para criação dos objetos
                campos: os campos que serao usados como parametros na criação
    
          Returns: List or Dict"""
        lista = []
        dicionario = {}

        try:
            with open(file, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

                mapa = {"standard-balls": Pokebola}

                for item, valor in dados.items():

                    if "categoria" in valor:
                        subclasse = mapa.get(valor["categoria"], classe)

                    else:
                        subclasse = classe

                    args = [item] + [valor.get(campo, None) for campo in campos]
                    obj = subclasse(*args)
                    
                    if file in ["mochila.json", "pokedex.json"]:
                        dicionario[obj.nome] = obj
                    else:
                        lista.append(obj)
                    
        except (json.JSONDecodeError, FileNotFoundError):
            pass

        return dicionario if file in ["mochila.json", "pokedex.json"] else lista

    @staticmethod
    def salvar(lista, file: str, funcao_dict):
        """Menu de salvamento dos json
    
          Args: file: o arquivo que vai ser aberto 
                lista: a lista que será utilizada para conversão dos objetos
                funcao_dict: a função auxiliar que ira fazer a conversão dos objetos 
    
          Returns: List or Dict"""
        with open(file, "w", encoding="utf-8") as arquivo:
            if isinstance(lista, list):
                dados = {obj.nome: funcao_dict(obj) for obj in lista}
            elif isinstance(lista, dict):
                dados = {nome: funcao_dict(obj) for nome, obj in lista.items()}
            else:
                dados = lista
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

    stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_json["stats"] | {"xp": 0}}
    tipos = [tipo['type']['name'] for tipo in pokemon_json['types']]

    Poke = Pokemon(pokemon_json["name"], tipos, stats)
    gamedata.lista_pokemon.append(Poke)

    gamedata.salvar_json(gamedata.lista_pokemon, "pokemons.json", lambda x:x.to_dict())

def criar_geracao():  #apenas um teste porque ainda nao tenho certeza de como quero fazer a criação dos pokemons, mas por enquanto vou trabalhar apenas com a primeira geração
    """
    Função que cria todos os pokemons da primeira geração (pode ser alterado para qualquer geração,
    basta mudar o parametro passado)
    e guarda em uma lista (lista_pokemons)
    
    Args:
        None

    Returns:
        None
    """
    geracao1 = get_all_generation(1)


    for i in geracao1["pokemon_species"]:
        pokemon_json = get_pokeapi(i["name"], "pokemon")

        can_learn = []

        for atk in pokemon_json["moves"]:
            for detail in atk["version_group_details"]:
                level_learned_at = detail["level_learned_at"]

            if level_learned_at > 0:
                obj_ataque = gamedata.get_ataque(atk["move"]["name"])
                if obj_ataque:
                    can_learn.append({"ataque": obj_ataque, "level_learned_at": level_learned_at})

        #aqui eu poderia ter feito diretamente a busca na api de ataques, no lugar de criar uma separada e salvar todos os ataques em uma lista separada
        #mas preferi deixar assim porque tava testando algumas coisas, não sei se vou mudar isso mais pra frente

        stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_json["stats"]}
        tipos = [tipo['type']['name'] for tipo in pokemon_json['types']]
            
        Poke = Pokemon(pokemon_json["name"], tipos, stats, can_learn)
        gamedata.lista_pokemon.append(Poke)

        gamedata.salvar(gamedata.lista_pokemon, "pokemons.json", lambda x:x.to_dict())


def criar_item(endpoint: str):
    """
    Função que cria um item atraves do nome ou id passado pelo usuario
    
    Args:
        None

    Returns:
        dict: Json da pokeapi
    """

    nome = pedir_input(endpoint)

    item_json = get_pokeapi(nome, endpoint)

    for item in gamedata.lista_items:
        if item_json["name"] == item.nome:
            print(f"{item_json["name"]} ja existe")
            return
        
    itens = Item(item_json["name"], item_json["cost"], item_json["category"]["name"], [item["name"] for item in item_json["attributes"]])
    gamedata.lista_items.append(itens)

    gamedata.salvar(gamedata.lista_items, "itens.json", lambda x:x.to_dict())

def criar_moves():
    """
    Função que cria todos os ataques
    
    Args:
        None

    Returns:
        dict: Json da pokeapi
    """
    ataque_json = get_pokeapi_move()

    for move_data in ataque_json["results"]:
        ataque_stats = get_move_stats(move_data["url"])

        obj_ataque = Ataques(move_data["name"], ataque_stats.get("damage", 0), ataque_stats["accuracy"], ataque_stats["damage_class"]["name"])
        if obj_ataque.nome in gamedata.lista_ataques:
            print(f"{obj_ataque.nome} já existe na lista")
        
        else:
            print(obj_ataque)
            gamedata.lista_ataques.append(obj_ataque)
            print(gamedata.lista_ataques)

    print(f"total de ataques transferidos: {len(gamedata.lista_ataques)}")

    gamedata.salvar(gamedata.lista_ataques, "ataques.json", lambda x:x.to_dict())

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

gamedata = GameData()

criar_geracao()