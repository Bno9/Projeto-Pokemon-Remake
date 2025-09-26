import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random

from Principal.Main_Menu import Fluxo, MenuState, MainMenu

#sistema simples e funcional para capturar pokemons e adiciona-los na pokedex
#ainda irei implementar level pra poder fazer o sistema de combate e melhora de atributos


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
            print("1 - Capturar pokemon\n" \
            "2 - Fugir\n" \
            "0 - Voltar")
            escolha = input("Escolha: ").strip()

            if escolha == "1":

                lista_pokebolas = [
                                    (item, valor) 
                                    for item, valor in gamedata.mochila.items()
                                    if valor.categoria == "standard-balls"
                                    ]

                if not lista_pokebolas:
                    print("Você não tem pokebolas")
                    return
            
                for numero, (pokebola, valor) in enumerate(lista_pokebolas, start=1):
                    print(f"{numero} - {pokebola} | quantidade: {valor.quantidade}")

                escolha_pokebola = int(input("Escolha qual pokebola deseja usar: ")) - 1

                if 0 <= escolha_pokebola < len(lista_pokebolas):
                    pokebola_escolhida = lista_pokebolas[escolha_pokebola][1]
                    if pokebola_escolhida.usar_pokebola(gamedata, pokemon_selvagem):
                        gamedata.pokedex.append(pokemon_selvagem)
                        
                        gamedata.salvar(gamedata.pokedex, "pokedex.json", lambda x:x.to_dict())
                
                    else:
                        break

                else:
                    print("Escolha uma opção válida")

            if escolha == "2":
                continue

            if escolha == "0":
                break