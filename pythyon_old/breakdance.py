#!/usr/bin/python3.7

cont = 0
while cont < 10:
    print("Execução{}".format(cont))
    if cont == 9:
        print("Interrompendo o loop com break")
        break
   
    cont += 1