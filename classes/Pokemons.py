import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

class Pokemon:
    def __init__(self, nome, tipos, stats, lista_ataques=None):
        self.nome = nome
        self.tipos = tipos
        self.stats = stats
        self.hp_atual = stats['hp']
        self.can_learn = lista_ataques
        self.ataques = []
        
        self.inicializar_ataques()

    def inicializar_ataques(self):
        if self.can_learn:
            for ataque in self.can_learn:
                if ataque["level_learned_at"] == 1 and len(self.ataques) < 2:
                        if ataque not in self.ataques:
                            self.ataques.append(ataque)
            for i in self.ataques:
                print(self.nome, i["ataque"].nome)

    def to_dict(self):
        return {
            "tipos": self.tipos,
                "stats": self.stats,
                "hp_atual": self.hp_atual,
                "can_learn": self.can_learn
                }


    def atacar(self, pokemon_inimigo, ataque):

        if pokemon_inimigo.hp_atual > 0:
        
            pokemon_inimigo.hp_atual -= ataque.dano
            print(f"{self} usou {ataque.nome} e deu {ataque.dano} em {pokemon_inimigo}")

        else:
            print(f"{self} foi derrotado")















    def to_dict(self):
        return {
            "tipos": self.tipos,
            "stats": self.stats,
            "hp_atual": self.hp_atual
        }

    def __str__(self):
        return f"{self.nome} | HP: {self.hp_atual}/{self.stats['hp']} | Tipos: {self.tipos}"


#fiz uma lista com todos ataques que o pokemon pode aprender
#a partir daqui é meio complicado porque ainda nao pensei em como vou fazer exatamente
#mas o plano seria criar os ataques padrões do pokemon
#criar o sistema de batalha
#sistema de xp e nivel
#e ai criar o sistema de ganhar ataques novos por level up
#pra finalizar, faço o sistema de vantagens e status
#depois de tudo isso, acredito que o jogo vai estar completo
#vou só mudar de json pra um banco de dados
#talvez usar rich pra deixar os textos mais bonitinhos
#e finalizar o projeto
#conforme forem surgindo ideias e bater vontade de mexer no código, eu vou melhorando ele