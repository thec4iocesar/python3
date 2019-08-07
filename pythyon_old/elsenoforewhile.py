#!/usr/bin/python3.7

nomes = ["caio", "billy", "tiwy", "ivan"]

busca = input("Digite o nome de uma pessoa:")

for nome in nomes:
    if busca.lower().strip() == nome:
        print("Convidado {} está na lista!".format(nome))
        break
else:
    print("Convidado {} não está na lista!!".format(busca))