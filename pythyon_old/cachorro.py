#!/usr/bin/python3.7

class Dog():
    '''Tentando abstrair um cachorro!'''
    dono = None

#usando o dunder init (double under init)
    def __init__(self,nome,raca,idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 10
        self.sede = 10
        self.fome = 10
    
    def __del__(self):
        print('Método destrutor executado!')

    def latir(self):
        print('Auau!')

    def andar(self):
        print('Andando...')
    
    def dormir(self):
        print('ZZZZzzz ; DND')
    
    def beber(self):
        print('GLUIBGLUIB')
    
    def comer(self):
        print('GIMME-SOME-MORE-OF-THAT-FOOD-YOU-MF')

dog1 = Dog('Ananias', 'Bull Terrier', 2)

#A Classe
print(type(dog1))

print('---------------------------------------------------------------------')

#Os métodos

print(dir(dog1))

print('---------------------------------------------------------------------')

#A documentação

print(dog1.__doc__)

print('---------------------------------------------------------------------')

print(dog1.dono)

dog1.dono = 'Caio'

print(dog1.dono)

print('---------------------------------------------------------------------')

print(dog1.nome, dog1.raca, dog1.idade, sep='\n')

print('---------------------------------------------------------------------')

dog1.andar()

print('---------------------------------------------------------------------')

print('Frenetik Mode ON, segure-se')

dog1.latir(), dog1.beber(), dog1.comer(), dog1.dormir()

print('---------------------------------------------------------------------')

print(dog1.nome, '''
    Energia{}
    Fome{}
    Sede{}
'''.format(dog1.energia, dog1.fome, dog1.sede))