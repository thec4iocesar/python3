#!/usr/bin/python3

import requests


URL = 'https://gen-net.herokuapp.com/api/users/auth'

payload = {
    'email': 'cuca@gmail.com',
    'password': '1234'
}
res = requests.post(URL, payload)

if res.status_code == 200:
    print(res.json())
else:
    print('Usuário/Senha invalido')