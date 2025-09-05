class MenuState:
    """Base para caso nao exista o execute em alguma classe.
    
    Args: menu: objeto que controla os estados da classe Menu
    
    Returns: Error
    """
    def execute(self, menu):
        raise NotImplementedError("Execute deve ser implementado.")


class MainMenu(MenuState):
    """Menu principal do jogo que controla todo fluxo
    
    Args: menu: objeto que controla os estados da classe Menu
    
    Returns: None"""

    def execute(self, menu):
        print("\n=== Menu Principal ===")
        print("1 - Loja")
        print("2 - Pokédex")
        print("0 - Sair")
        escolha = input("Escolha: ").strip()

        if escolha == "1":
            menu.change_state(ShopMenu())
        elif escolha == "2":
            menu.change_state(PokedexMenu())
        elif escolha == "0":
            menu.running = False
        else:
            print("Opção inválida. Tente novamente.")


class ShopMenu(MenuState):
    """Menu da loja, irei implementar a compra de itens
    
    Args: menu: objeto que controla os estados da classe Menu
    
    Returns: None"""

    def execute(self, menu):
        print("\n=== Loja ===")
        print("1 - Comprar (placeholder)")
        print("0 - Voltar")
        escolha = input("Escolha: ").strip()

        if escolha == "0":
            menu.change_state(MainMenu())
        else:
            print("Compra simulada")

class PokedexMenu(MenuState):
    """Menu da pokedex, ainda não tenho certeza do que vou fazer aqui, mas ja deixei a base"""
    def execute(self, menu):
        print("\n=== Pokédex (exemplo) ===")


class Menu:
    def __init__(self):
        self.state = MainMenu()   #Estado inicial
        self.running = True

    def change_state(self, new_state):
        self.state = new_state

    def run(self):
        while self.running:
            try:
                self.state.execute(self)
            except KeyboardInterrupt:
                print("\nInterrompido pelo usuário. Saindo...")
                self.running = False


if __name__ == "__main__":
    menu = Menu()
    menu.run()
    print("Menu encerrado.")
