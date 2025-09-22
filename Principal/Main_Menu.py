import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.Load_Save import GameData
from datetime import datetime, timedelta

class MenuState:
    """Base para caso nao exista o execute em alguma classe.
    
    Args: menu: objeto que controla os estados da classe Menu
    
    Returns: Error
    """
    def execute(self, *args):
        raise NotImplementedError("Execute deve ser implementado.")

class MainMenu(MenuState):
    """Menu principal do jogo que controla todo fluxo
    
    Args: menu: objeto que controla os estados da classe Menu
    
    Returns: None"""

    def execute(self, menu, gamedata):
        print("\n=== Menu Principal ===")
        print("1 - Capturar Pokemons")
        print("2 - Loja")
        print("3 - Pokédex")
        print("0 - Sair")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            from Principal.Capturar import CapturarMenu
            menu.change_state(CapturarMenu())
        elif escolha == "2":
            from Principal.Loja import ShopMenu
            menu.change_state(ShopMenu())
        elif escolha == "3":
            menu.change_state(PokedexMenu())
        elif escolha == "0":
            menu.running = False
        else:
            print("Opção inválida. Tente novamente.")

class PokedexMenu(MenuState):
    """Menu da pokedex, ainda não tenho certeza do que vou fazer aqui, mas ja deixei a base"""
    def execute(self, menu, gamedata):
        print("\n=== Pokédex (exemplo) ===")

class Fluxo:
    def __init__(self):
        self.state = MainMenu()   #Estado inicial
        self.running = True
        self.game_data = GameData()
        self.hora_atualizacao = datetime.now() + timedelta(seconds=0) #Deixei pra loja iniciar com um estoque por padrão para fazer testes mais facilmente, depois volto ao normal

    def change_state(self, new_state):
        self.state = new_state


    #Loop que controla o estado do menu
    def run(self):
        while self.running:
            try:
                self.state.execute(self, self.game_data)
            except KeyboardInterrupt:
                print("\nInterrompido pelo usuário. Saindo...")
                self.running = False


if __name__ == "__main__":
    menu = Fluxo()
    menu.run()
    print("Menu encerrado.")

