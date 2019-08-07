#!/usr/bin/python3.7

import os

print("----------------------------")

#Método getlogin retorna o current process’s real user id.

print('UID', os.getuid(), sep=':')

print("----------------------------")

#Método listdir retorna um objeto list com a lista de diretorios e arquivos
# no caminho informado. se o parametro caminho nao for informado retornada o list do 
# diretorio atual 

print('Listar diretorio', os.listdir(), sep=': ')
print('Listar diretorio', os.listdir('/home/developer'), sep=': ')

print("----------------------------")

#Criando diretorios

print('Criar diretorio', os.mkdir('pythondir'), sep=': ')
print('Criar diretorio', os.mkdir('pythondir2'), sep=': ')

#Gravando um arquivo

with open('pythondir2/testemodulo.txt', 'w') as arquivo:
    arquivo.write('teste')

#Renomeando dirs
print('Renomear diretorio', os.rename('pythondir', 'pythonrenomeado'), sep=': ')

#Renomeando arquivo
print('Renomear Arquivo', os.rename('pythondir2/testemodulo.txt','pythondir2/renomemodulo.txt'), sep=': ')

print("----------------------------")

#Executando comandos do S.O.
os.system('sudo apt-get update')

print("----------------------------")