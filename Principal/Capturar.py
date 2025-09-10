import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random

from Principal.Main_Menu import Fluxo, MenuState, MainMenu


class CapturarMenu(MenuState):
    """Menu de captura de pokemons
    
    Args: menu: objeto que controla os estados da classe Menu
    
    Returns: gamedata"""
     
    def captura(self, menu, gamedata):
        while True:
            
            pokemon_selvagem = random.choice(gamedata.lista_pokemon)

            escolha = input(f"Um {pokemon_selvagem} apareceu, deseja captura-lo?\n1-Capturar\n2-Fugir\n3-Voltar ao menu principal").strip()

            if escolha == 1:
                for item, valor in gamedata.mochila:
                    if item["poke-ball"] and valor["quantidade"] > 0:
                        pass

            if escolha == 2:
                continue

            if escolha == 3:
                menu.change_state(MainMenu())
