#!/usr/bin/python3.7

nome = input("Digite seu nome:")
print("{}, ***** ".format(nome))

ling = input("Digite a melhor linguagem de programação:")

if ling.lower().strip() == 'python':
    print("{}, *** {} *** !".format(nome,ling))

else:
    print("{}, burro ,{} é chato. Tente novamente escrevendo para a resposta surpresa".format(nome,ling))