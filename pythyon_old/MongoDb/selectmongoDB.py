#!/usr/bin/python3

from pymongo import MongoClient

from pprint import pprint
# Aqui optamos COM ou SEM pretty

try:
    con = MongoClient()
    db = con['projeto']

except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    #printa tudo
    # for x in db.pessoas.find():
    #     print(x)
    #     # pprint(x)

    #printa a query exata
    pprint([usuario for usuario
    in db.pessoas.find({"_id":1122123})])

except Exception as e:
    print('Erro: {}'.format(e))