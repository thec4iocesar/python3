#!/usr/bin/python3

from pymongo import MongoClient

try:
    con = MongoClient()
    db = con['projeto']

except Exception as e:
    print('Erro: {}'.format(e))
    exit()

try:
    a = db.pessoas
    print(.find(a())
    
for x in mydoc:
  print(x)

except Exception as e:
    print('Erro: {}'.format(e))