import random
from datetime import datetime, timedelta
import time

itens = ["banana", "pera", "maca", "ovo", "uva", "laranja"]

def loja():
    loja_atual = random.choices(itens, k=3)

    ultimo_update = datetime.now()


    while True:

        print(loja_atual, datetime.now())

        novo_loja = atualizar_loja(loja_atual, ultimo_update)

        if novo_loja:
            loja_atual = novo_loja
            ultimo_update = datetime.now()

        time.sleep(5)


def atualizar_loja(loja_atual,ultimo_update):

    atualizar =  ultimo_update + timedelta(seconds=30)

    if datetime.now() >= atualizar:
        print("Atualizando loja")
        loja_atual = random.choices(itens, k=3)
        print(f"itens novos na loja: {loja_atual}")
        return loja_atual
    else:
        return False

loja()


