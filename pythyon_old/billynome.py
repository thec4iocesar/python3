#!/usr/bin/python3.7

nome = input("Digite seu nome:")
print("{}, ola".format(nome))

ling = input("Digite a melhor linguagem de programação:")

if ling.lower().strip() == 'python':
    print("{}, ERROU {} nao é!".format(nome,ling))

else:
    print("{}, não,{} é chato. Tente novamente escrevendo para a resposta surpresa".format(nome,ling))