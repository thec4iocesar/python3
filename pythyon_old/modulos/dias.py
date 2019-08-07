#!/usr/bin/python3.7

from datetime import datetime
from datetime import date

print('-----------------------------------------------------')

print('Data atual', datetime.now(), sep=': ')

print('-----------------------------------------------------')

print('Data atual formatdata', datetime.now().strftime('%d/%m/%Y %H:%M:%S'), sep=': ')

print('-----------------------------------------------------')

hoje = date.today()

#calculando hoje +d45

data_final = date.fromordinal(hoje.toordinal() + 45)
diferenca = data_final - hoje

print('Inicio {}\n Fim {}\nDiferença {} dias'\
     .format(hoje.strftime('%d/%m/%Y'),
     data_final.strftime('d%/%m/%Y'),
     diferenca.days))

print('-----------------------------------------------------')

data_nascimento = date(1989,10,17)
hoje = date.today()
dias = hoje - data_nascimento
idade = int(dias.days /365)

print('Idade: {} anos'.format(idade))

print('-----------------------------------------------------')