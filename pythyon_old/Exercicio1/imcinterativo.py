#!/usr/bin/python3.6

from art import *

nome = input('Por favor, digite seu nome:')
peso = float(input('Digite seu peso em KG, por favor:'))
altura = float(input('Digite sua altura em metros, por favor:'))

imc = (peso)/(altura*altura)
nomealterado = (nome + ' Otariano')

print ('{}, seu imc e:'.format(nomealterado))
print (imc)
print ('executamos diversos testes e .... \n \
        ........ de acordo com nossos especialistas \n \
        ......... voce .......')

if imc <= 18.5:
        classificacao_de_gordice='Esta  muito magro!'
elif imc <= 24.9:
        classificacao_de_gordice='Esta  no shape!'
elif imc <= 29.9:
        classificacao_de_gordice='Possui  tetas, seu animal!'
elif imc <= 34.9:
         classificacao_de_gordice='Esta  rolito!'
elif imc <= 39.9:
        classificacao_de_gordice='Esta  obeso!'
else:
      classificacao_de_gordice='Esta  em  Stewy  Mode, \n vai  morrer'
	  
tprint (classificacao_de_gordice)