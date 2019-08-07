#!/usr/bin/python3.7

class Carro():
    __proprietario = 'Caio'

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 'flex'

    def __del__(sef):
        print('Método destructor executado!')
    
    def acelerar(self):
        print('VRUM')
    
    def freiar(self):
        print('Freiando!')
    
    def getProprietario(self):
        return self.__proprietario
    
    def setProprietario(self, proprietario):
        self.__proprietario = proprietario
    
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        self.combustivel = 'eletrico'
    
    def acelerar(self):
        print('Sniiiiiiiif....')

car1 = Carro('Volkswagem', 'Up', 2018)

print(car1.modelo,car1.combustivel)

car1.acelerar()

print('Proprietário', car1.getProprietario(), sep='\n')

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

car2 = CarroEletrico('GM', 'Bolt', 2018)

print(car2.modelo, car2.combustivel)
car2.acelerar()

print('Proprietario', car2.getProprietario(), sep='\n')

#Alterando o Proprietario com Input

proprietario = input('Informe o dono da caranga {}:'.format(car2.modelo))

car2.setProprietario(proprietario.strip())

print('Proprietario', car2.getProprietario(),'Alterado', sep='\n')

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')