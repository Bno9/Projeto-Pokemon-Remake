import math 

def media(*args):
    total = sum(args)

    return total / len(args)


print(media(5, 10, 15))  # 10
print(media(2, 4, 6, 8))


def apresentar(**kwargs):

    for i, valor in kwargs.items():
        print(f"Informações {i} - {valor}")

apresentar(nome="Breno", idade=21, cidade="São Paulo")


calc = lambda op, *nums: (sum(nums) if op == "soma" else
                          math.prod(nums) if op == "multiplica" else
                          sum(nums) / len(nums) if op == "media" else
                          print("operador invalido"))
    
print(calc("soma", 2, 4, 6))        # 12
print(calc("multiplica", 2, 3, 4))  # 24
print(calc("media", 5, 10, 15)) 



def extremos(*args):
    
    ordenado = sorted(args)

    return ordenado[0], ordenado[-1]

    return max(args), min(args)


print(extremos(4, 7, 1, 9, 2))


def concat(*args):
        return " - ".join(args)


print(concat("Python", "é", "legal"))  

def apresentacao(**kwargs):
    for i, valor in kwargs.items():
        print(f"{i}: {valor}")



apresentacao(nome="Breno", idade=21, cidade="SP")


def config_jogo(**kwargs):
    defaults = {
        "dificuldade": "normal",
        "som": True,
        "resolucao": "720p"
    }
    
    # atualiza os padrões com o que foi passado
    defaults.update(kwargs)
    
    # mostra as configurações
    for chave, valor in defaults.items():
        print(f"{chave}: {valor}")

config_jogo(dificuldade="hard", som=True, resolucao="1080p")
    

def relatorio(*args, **kwargs):
     
    print(f"soma total: {sum(args)}")

    for chave, valor in kwargs.items():
        print(f"{chave} - {valor}")


relatorio(10, 20, 30, nome="Breno", idade=21)
# "Soma total: 60"
# "nome: Breno"
# "idade: 21"


def tempo_atualizacao(func):
    def wrapper():
        pass