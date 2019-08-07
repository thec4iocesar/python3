#!/usr/bin/python3

from pymongo import MongoClient

try:
    con = MongoClient()
    db = con['projeto']

except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    db.pessoas.insert(
        {
            '_id':69,
            'nome': 'Jonny',
            'dtnasc': 'WHATEVER'
        }
     )

except Exception as e:
    print('Erro: {}'.format(e))