import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class Ataques:
    def __init__(self, nome, dano, precisao, tipo):
        self.nome = nome
        self.dano = dano
        self.precisao = precisao
        self.tipo = tipo

    def to_dict(self):
        return {
            "dano": self.dano,
            "precisao": self.precisao,
            "tipo": self.tipo
        }
    
    def get_ataque(self, nome_ataque):
        from utils.Load_Save import gamedata
        for ataque in gamedata.lista_ataques:
            if nome_ataque == ataque.nome:
                return ataque
            return None

    def __str__(self):
        return f"{self.nome} - dano: {self.dano} - precisao: {self.precisao} - tipo ataque: {self.tipo}"