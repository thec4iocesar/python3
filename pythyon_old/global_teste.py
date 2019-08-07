#!/usr/bin/python3.7

nome = "Anonimo"

#com global, ele usa o nome de Ivan nas duas, sem global um para cada!

def boas_vindas():
    global nome
    nome = "Ivan"
    print("Seja bem vindo, {}!".format(nome))

boas_vindas()
print(nome)