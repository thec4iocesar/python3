#!/usr/bin/python3

#criação do arquivo frutas em modo escrita , escrevendo banana + enter

arquivo = open('frutas.txt', 'w')

arquivo.write('Banana\n')

arquivo.close()

#append na escrita do arquivo
#lembrando que o as vai setar uma nova variavel. isso eh dinamico, cada hora
#que eu boto "as", ele vai setar uma nova variavel para o "arquivo"

with open("frutas.txt", "a") as arquivo:
    arquivo.write("limão\n")
    arquivo.write("melancia\n")

with open("frutas.txt", "r") as arquivo:
    print(arquivo.read())

# brincando com readlines

with open("frutas.txt", "r") as arquivo:
    print(arquivo.readlines())

nomes = ["João", "Maria", "Pedro"]

#criando arquivo com x, mas sem espaco

with open("nomes.txt", "x") as arquivo:
    arquivo.writelines(nomes)

#criando arquivo com espaco

with open("nomes.txt", "w") as arquivo:
     for nome in nomes:
         arquivo.write(nome + "\n")

import os
myCmd = 'zip file.zip *.txt'
os.system(myCmd)