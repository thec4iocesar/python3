#!/usr/bin/python3

import requests


URL = 'https://gen-net.herokuapp.com/api/users'
res = requests.get(URL)

for u in res.json():
    print(u.get('name'))
