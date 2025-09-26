import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random

from utils.Load_Save import gamedata
from Principal.Main_Menu import MenuState, MainMenu


class BatalhaMenu(MenuState):

    def execute(self, menu, gamedata):
            
            print("\n=== Batalha ===")
            print("1 - Batalhar")
            print("0 - Voltar")

            escolha = input("Escolha: ").strip()

            if escolha == "1":
                self.lutar(menu,gamedata)

            elif escolha == "0":
                menu.change_state(MainMenu())

            else:
                print("Opção inválida")

    def lutar(self,menu,gamedata):
                while True:

                    pokemon_aliado = gamedata.pokedex[0] # só pra testar, depois vou arrumar

                    pokemon_inimigo = random.choice(gamedata.lista_pokemon)
                    level = 0 #deixei padrão, mas vou mudar

                    lutar = input(f"Um {pokemon_inimigo.nome} de level: {level} apareceu. Digite 1 para lutar e 0 para fugir\n").strip()

                    if lutar == "1":

                        print(f"Você jogou seu {pokemon_aliado}")

                        while True:

                            escolha = input("O que deseja fazer?\n" \
                                            "1- Atacar\n" \
                                            "2- Mudar pokemon\n" \
                                            "3- Usar item\n" \
                                            "4- Fugir\n").strip()

                            if escolha == "1":
                                for enum, i in enumerate(pokemon_aliado.ataques, start=1): #a lista ta vindo vazia, e acredito que seja por causa do None na criação da classe (preciso arrumar o load dos pokemons)
                                    print(f"{enum} - {i}")

                                escolha = int(input("Digite o numero do ataque que deseja utilizar: "))

                                ataque_escolhido = pokemon_aliado.ataques[escolha - 1]

                                pokemon_aliado.atacar(self, pokemon_inimigo, ataque_escolhido) #falta criar o método de ataque

                            elif escolha == "2":
                                for num, i in enumerate(gamedata.pokedex): #aqui vai ser a lógica pra trocar o pokemon selecionado
                                    print(f"{num} - {i}")

                            elif escolha == "3":
                                pass #tenho os itens criados, mas falta a logica de usar eles

                            elif escolha == "4":
                                return

                            else:
                                print("Opção inválida")

                    elif lutar == "0":
                        break

                    else:
                        print("Opção inválida")
                    
            

    

