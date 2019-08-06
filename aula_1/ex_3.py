
import requests


URL = 'https://gen-net.herokuapp.com/api/users'
res = requests.post(URL, {
    'name': 'Lucas Ricciardi de Salles',
    'email': 'lucas@naoexiste.com',
    'password': '123'
})

print(res.status_code)
print(res.text)
