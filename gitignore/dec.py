import time
from datetime import datetime, date
import random

def teste(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

def medir_tempo(func):
    def wrapper():
        inicio = datetime.now()
        func()
        fim = datetime.now()
        print(f"Tempo de execução: {fim - inicio}")
    return wrapper

def checagem(func):
    def wrapper(*args):
        for numeros in args:
            if not isinstance(numeros, (int, float)):
                print("Erro: todos os parâmetros devem ser números")
                return
        return func(*args)
    return wrapper


def repetir(func):
    def wrapper():
        for _ in range(3):
            func()
    return wrapper

def cache_decorator(func):
    dicionario = {}

    def wrapper(x):
        if x in dicionario:
            print(f"Usando cache em memoria para {x}:")
            return dicionario[x]

        resultado = func(x)
        dicionario[x] = resultado
        return resultado
        
    return wrapper

def print_n(n):
    def decorador(func):
        def wrapper(*args):
            for _ in range(n):
                func(*args)
        return wrapper
    return decorador




@print_n
def printar(n):
    print("Ola!")

@cache_decorator
def potencia(x):
    return x ** 2

@repetir
def loop():
    print("Executando...")

@checagem
def soma(a, b):
    return a + b

@medir_tempo
def tempo():
    time.sleep(2)
    print("Função finalizada")

@teste
def oi():
    print("oi")

oi()
tempo()
print(soma(5, 7))
soma(5, "7")
loop()
print(potencia(4))  
print(potencia(4)) 
print(potencia(5))
print(potencia(5))
print(potencia(random.randint(0,100)))
printar(4)