
import requests


payload = {
    'name': input('Digite um nome para o usuário 2: '),
    'password': '1234'
}

URL = 'https://gen-net.herokuapp.com/api/users/2'


res = requests.put(URL, payload)

if res.status_code == 200:
    print(res.json())
