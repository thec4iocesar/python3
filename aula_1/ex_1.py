
import requests


cep = input('Digite seu cep: ')

URL = 'https://viacep.com.br/ws/{}/json/'.format(cep)
res = requests.get(URL)

print(res.json().get('logradouro'))