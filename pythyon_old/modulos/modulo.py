#!/usr/bin/python3.7

print('Usando Modulos')

def contagem():
    a = 0
    while a <= 10:
        print (a)
        a = a + 1
contagem()

def somar(x, y):
    print("somando")
    return x + y

def boas_vindas(nome):
    return 'Seja bem vindo, {}!'\
        .format(nome)