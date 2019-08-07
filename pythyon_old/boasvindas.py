#!/usr/bin/python3.7

def boas_vindas(nome):
    print("Seja bem vindo, {}!".format(nome))

# boas_vindas('Ivan')

nome = input("Informe seu nome, por favor:")
boas_vindas(nome)

# boas_vindas()