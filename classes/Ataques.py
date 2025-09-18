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

    def __str__(self):
        return f"{self.nome} - dano: {self.dano} - precisao: {self.precisao} - tipo ataque: {self.tipo}"