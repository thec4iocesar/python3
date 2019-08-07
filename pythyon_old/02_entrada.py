#!/usr/bin/python3.7

nome = input('Digite seu nome: ')

if (nome == "Caio"):
    print('Bem vindo {}!'.format(nome))
    print ("Hello", nome, 10.5, sep='AUAU', end='\n\n\n\n\n')

#sep = separador de itens
#end fim de linha

linguagem = input("Qual a melhor linguagem de programação?")

if linguagem == "python" or "Python":
    print("Acerto Miseravi")

elif linguagem == "C#":
    print("C# é zuado")

elif linguagem == "C++":
    print("Micreiro")

else:
    print("Erooou")

nome = nome.replace('a', '@')
print(nome)

nome = 'X'.join(nome)
print(nome)

letras=['a', 'b', 'c', 'd']
letras.insert(0, 'Caio')

print(letras)

numero = letras.count('a')
print(numero)

cliente={'nick': 'Billy', 'sobrenome': 'PauMole', 'dtnasc': '2017-05-15'}
print(cliente['nick'],cliente['sobrenome'])