
import requests

userid = input('Digite seu id: ')

URL = 'https://gen-net.herokuapp.com/api/users/{}'.format(userid)
res = requests.get(URL)

if res.status_code == 200:
    print(res.json())

elif res.status_code == 404:
    print('Usuário não encontrado')

else:
    print('Requisição inválida')

