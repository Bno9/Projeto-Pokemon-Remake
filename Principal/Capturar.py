import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random

from Principal.Main_Menu import Fluxo, MenuState, MainMenu



#sistema simples e funcional para capturar pokemons e adiciona-los na pokedex
#ainda irei implementar level pra poder fazer o sistema de combate e melhora de atributos
#tambem vou implementar a captura com os outros tipos de pokebola, e uma chance especifica pra cada pokebola


class CapturarMenu(MenuState):
    """Menu de captura de pokemons
    
    Args: menu: objeto que controla os estados da classe Menu
          gamedata: objeto que controla todas informações do jogo
    
    Returns: None"""

    def execute(self, menu, gamedata):
        print("\n=== Capturar pokemons ===")
        print("1 - Buscar pokemon")
        print("0 - Voltar")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            self.captura(menu, gamedata)

        if escolha == "0":
             menu.change_state(MainMenu())
     
    def captura(self, menu, gamedata):
        """Menu de captura de pokemons
    
          Args: menu: objeto que controla os estados da classe Menu
          gamedata: objeto que controla todas informações do jogo
    
          Returns: None"""
        while True:
            pokemon_selvagem = random.choice(gamedata.lista_pokemon)

            print(f"Um {pokemon_selvagem} apareceu")
            print("1 - Capturar pokemon")
            print("2 - Fugir")
            print("0 - Voltar")
            escolha = input("Escolha: ").strip()

            if escolha == "1":
                if self.usar_pokebola(gamedata):
                    gamedata.pokedex[pokemon_selvagem.nome] = {"nome": pokemon_selvagem.nome,
                                                               "tipos": pokemon_selvagem.tipos,
                                                               "stats": pokemon_selvagem.stats,
                                                               "hp_atual": pokemon_selvagem.hp_atual}
                    
                    gamedata.salvar(gamedata.pokedex, "pokedex.json", lambda x: x)
                
                else:
                    break

            if escolha == "2":
                continue

            if escolha == "0":
                break


    def usar_pokebola(self, gamedata):
        """Menu de uso de pokebolas
    
          Args: menu: objeto que controla os estados da classe Menu
          gamedata: objeto que controla todas informações do jogo
    
          Returns: Boolean"""
        
        for item, valor in gamedata.mochila.items():
            if item == "poke-ball" and valor["quantidade"] > 0:
                valor["quantidade"] -= 1
                print("Você usou uma pokebola")
                gamedata.salvar(gamedata.mochila, "mochila.json", lambda x: x)
                return True

        print("Você não tem pokebolas")
        return False
