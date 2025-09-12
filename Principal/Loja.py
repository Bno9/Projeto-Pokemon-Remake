import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random
from datetime import datetime, timedelta

from Principal.Main_Menu import Fluxo, MenuState, MainMenu #Importei a variavel hora_atualização só pra teste, mas quero fazer de um jeito mais organizado depois

class ShopMenu(MenuState):
    """Menu da loja
    
    Args: menu: objeto que controla os estados da classe Menu
          gamedata: objeto que controla todas informações do jogo
    
    Returns: None"""

    def execute(self, menu, gamedata):
        print("\n=== Loja ===")
        print("1 - Comprar")
        print("0 - Voltar")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            while True:
                gamedata.estoque = self.atualizar_loja(gamedata.estoque, gamedata.lista_items, menu)

                if not gamedata.estoque:
                    print(f"A loja está sem estoque no momento. Volte novamente as {menu.hora_atualizacao.strftime("%H:%M:%S")}")
                    break

                print(f"A loja ira atualizar as: {menu.hora_atualizacao}. Itens disponives na loja:")
                for numero, item in enumerate(gamedata.estoque, start=1):
                    print(f"{numero} - {item} - preço: {item.custo}")
               
                compra = int(input("Digite o numero de qual item deseja comprar, ou digite 0 se quiser voltar: ")) - 1

                if compra == -1:
                    break

                quantidade = int(input("Digite quantos itens deseja comprar: "))

                item_escolhido = gamedata.estoque[compra]

                if gamedata.dinheiro >= item_escolhido.custo * quantidade:
                    if item_escolhido.nome in gamedata.mochila:
                        gamedata.mochila[item_escolhido.nome]["quantidade"] += quantidade
                    else:
                        gamedata.mochila[item_escolhido.nome] = {"valor_venda": item_escolhido.custo / 2,
                                                            "quantidade": quantidade,
                                                            "categoria": item_escolhido.categoria,
                                                            "atributos": item_escolhido.atributos}
                
                gamedata.salvar(gamedata.mochila, "mochila.json", lambda x: x)

                print(f"Você comprou {quantidade} {item_escolhido.nome}, e gastou {item_escolhido.custo * quantidade}")
                break
                    
        elif escolha == "0":
            menu.change_state(MainMenu())

        else:
            print("Opção inválida")


    def atualizar_loja(self, estoque, lista_items: list, menu) -> list :
        """Função auxilixar que atualiza a loja
        
        Args: estoque: Objeto do gamedata com o estoque atual da loja
            lista_items: Objeto do gamedata com informação de cada item existente
            menu: Objeto que controla os estados das classes menu
        
        Returns: List"""
        
        hora_atual = datetime.now()

        if hora_atual >= menu.hora_atualizacao:
            itens_disponiveis = []
            for _ in range (0,3):
                while True:
                    item_aleatorio = random.choice(lista_items)  #descobri que poderia usar random.sample no lugar de fazer essa lógica, mas agora prefiro deixar desse jeito
                    if item_aleatorio.custo <= 0:
                        continue
                    if item_aleatorio not in itens_disponiveis:
                        itens_disponiveis.append(item_aleatorio)
                        break
                    else:
                        continue

            menu.hora_atualizacao = hora_atual + timedelta(seconds=30)
            return itens_disponiveis
        
        return estoque