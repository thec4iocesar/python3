#!/usr/bin/python3.7

def cadastro(**pessoa):
    #return pessoa
    #return type(pessoa)
    return "O usuário {} {} com a idade de {} foi cadastrado com sucesso!"\
        .format(pessoa["nome"], pessoa["sobrenome"], pessoa["idade"])

print(cadastro(nome='Ivan',sobrenome="Ferro",idade="43"))

def cadastro(pessoa):
    #return pessoa
    #return type pessoa
    return "O usuario {} {}, foi cadastrado com sucesso!"\
        .format(pessoa["nome"], pessoa["sobrenome"])

pessoa = {
            'nome':'Ivan',
            'sobrenome':'Ferro'
            'idade: 43'
            }

print(cadastro(pessoa))