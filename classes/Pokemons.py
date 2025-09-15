import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class Pokemon:
    def __init__(self, nome, tipos, stats):
        self.nome = nome
        self.tipos = tipos
        self.stats = stats
        self.hp_atual = stats['hp']

    def to_dict(self):
        return {
            "tipos": self.tipos,
            "stats": self.stats,
            "hp_atual": self.hp_atual
        }

    def __str__(self):
        return f"{self.nome} | HP: {self.hp_atual}/{self.stats['hp']} | Tipos: {self.tipos}"