#!/usr/bin/python3

from pymongo import MongoClient

try:
    con = MongoClient()
    db = con['projeto']

except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    db.pessoas.delete_one(
        {'_id':21122123}
        )

except Exception as e:
    print('Erro: {}'.format(e))