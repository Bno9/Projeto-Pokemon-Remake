import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class Item:
    def __init__(self, nome, custo, categoria, atributos):
        self.nome = nome
        self.custo = custo
        self.categoria = categoria
        self.atributos = atributos

    def __str__(self):
        return f"{self.nome} | Preço: {self.custo} | Categoria: {self.categoria} | Atributos: {self.atributos if self.atributos else "Nenhum"}"