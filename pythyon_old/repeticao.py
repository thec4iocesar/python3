#!/usr/bin/python3.7

idade = int(input('Digite sua idade: '))
habilitacao = (input('Voce e habilitado? Sim ou Nao? '))
dirigir = False

if habilitacao.lower().strip() == 'sim':
    habilitacao = True

else:
    instrutor = input('Voce esta acompanhado de um instruto? Sim ou nao?')
    if instrutor.lower().strip() == 'sim':
        dirigir = True

if idade >= 18 and habilitacao == True:
        print('Voce pode dirigir')

elif dirigir:
    print('Boa aula')

else:
    print('Voce nao pode dirigir')