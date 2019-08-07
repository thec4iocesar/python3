#!/usr/bin/python3.7

for x in range(11):
    print(x)

print("-----------------------------------------------------")

#range(inicio, fim)

for x in range(1,11):
    print(x)

print("-----------------------------------------------------")

#range(inicio, fim, incremento)
#ou seja, conta de 2 ate 11 de 2 em 2

for x in range(2,11,2):
    print(x)

print("-----------------------------------------------------")

#range (inicio, fim, incremento) contagem decrescente
for x in range (10,1,-2):
    print(x)

print("-----------------------------------------------------")

#range (inicio, fim) imprimindo caracteres
for x in range(97, 97 + 26):
    print(chr(x))

print("-----------------------------------------------------")

#range (inicio, fim) criando uma lista
letras = []

for x in range (97, 97 + 26):
    letras.append(chr(x))

print(letras)

print("-----------------------------------------------------")

frutas = ["Manga", "Abacaxi", "Uva", "Banana", "Morango", "Xoxota"]

for num, item in enumerate(frutas):
    print ("{} está na mesa{}".format(item,num))

print("-----------------------------------------------------")

letras = []

for x in range (1,100):
    letras.append(chr(x))

print(letras)