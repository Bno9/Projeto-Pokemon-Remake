import random

# nums = [1, 2, 3, 4, 5]


# def impares(n):
#     for i in range(n):
#         if i % 2 == 1:
#             yield i

# for i in impares(10):
#     print(i)


# def quadrados(lista):
#     for numero in lista:
#         yield numero * numero


# for q in quadrados(nums):
#     print(q)


def baralho(embaralhar=False):
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    naipes = ["♠", "♥", "♦", "♣"]

    cartas = [v + n for n in naipes for v in valores]  # combina todos os valores e naipes

    if embaralhar:
        random.shuffle(cartas)  # embaralha as cartas

    for carta in cartas:
        yield carta  # devolve uma carta por vez

meu_baralho = baralho(embaralhar=True)

print(next(meu_baralho))  # tira a primeira carta
print(next(meu_baralho))  # tira a segunda carta

# Ou iterando:
for carta in baralho():
    print(carta)
