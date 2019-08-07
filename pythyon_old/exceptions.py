#!/usr/bin/python3.7

while True:
    num = input('Digite um número, fazendo favor:')

    if num == "exit":
        break
    
    # if num.isnumeric():
    #     print(int(num) + 2)
    
    # else:
    #     print("Você digitou {}, isso não é um número. DIGITE UM NÚMERO".format(num))

    try:
         print(int(num) *2)
    
    except Exception as e:
        print(e)
        print("Você digitou {}, isso não é um número. DIGITE UM NÚMERO".format(num))