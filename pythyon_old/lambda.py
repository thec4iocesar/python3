#!/usr/bin/python3.7


#ao inves de

def soma(x, y):
    return x + y

print(soma(5,6))

print("AGORA COM LAMBDA")

a = lambda x, y: x + y

print(a(5,6))

print("-------------------------------------------------------------------------")

print((lambda x: x ** 2)(3))

print("-------------------------------------------------------------------------")

for x in range(1, 11):
    print((lambda x: x ** 2)(x))

print("-------------------------------------------------------------------------")

quadrado = []
for x in range(1, 11):
    quadrado.append((lambda x: x ** 2)(x))

print(quadrado)

print("-------------------------------------------------------------------------")

quadrado = list(map(lambda x: x ** 2, range(1,100)))

print(quadrado)