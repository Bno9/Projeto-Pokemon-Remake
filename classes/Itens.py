import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import random

class Item:
    def __init__(self, nome, custo, categoria, atributos, quantidade=0):
        self.nome = nome
        self.custo = custo
        self.categoria = categoria
        self.atributos = atributos
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "custo": self.custo,
            "categoria": self.categoria,
            "atributos": self.atributos,
            "quantidade": self.quantidade
        }

    def __str__(self):
        return f"{self.nome} | Preço: {self.custo} | Categoria: {self.categoria} | Atributos: {self.atributos if self.atributos else "Nenhum"}"
        

class Pokebola(Item):
    def __init__(self, nome, custo, categoria, atributos, quantidade, chance_captura=0):
        super().__init__(nome, custo, categoria, atributos, quantidade)
        self.chance_captura = chance_captura or chance_pokebolas.get(nome, 0.1)

    def to_dict(self):
        base = super().to_dict()
        base.update({
            "chance_captura": self.chance_captura
        })
        return base

    
    def usar_pokebola(self, gamedata, pokemon):
        """Menu de uso de pokebolas
    
          Args: menu: objeto que controla os estados da classe Menu
          gamedata: objeto que controla todas informações do jogo
    
          Returns: Boolean"""
        
        sucesso = random.randint(1,100)

        if self.quantidade > 0 and sucesso <= self.chance_captura:  
            self.quantidade -= 1
            print(f"Você usou uma {self.nome} e capturou {pokemon.nome}")

        elif self.quantidade > 0 and sucesso > self.chance_captura:
            self.quantidade -= 1
            print(f"Você usou {self.nome}, mas o pokemon {pokemon.nome} conseguiu escapar\n")
            gamedata.salvar(gamedata.mochila, "mochila.json", lambda x:x.to_dict())
            return False

        else:
            print(f"Você não tem mais {self.nome}")
            return False
        
        gamedata.salvar(gamedata.mochila, "mochila.json", lambda x:x.to_dict())

        return True
    
    def __str__(self):
        return f"{self.nome} - chance de captura: {self.chance_captura}% - valor de venda {self.custo / 2}"


    
chance_pokebolas = {"poke-ball": 20,
                        "great-ball": 35,
                        "ultra-ball": 50,
                        "master-ball": 100,
                        "safari-ball": 25,
                        "repeat-ball": 40}