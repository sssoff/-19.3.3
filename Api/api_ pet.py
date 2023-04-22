
import requests
import json
#
# # POST-запрос на создание нового пользователя
#
# params ={
#     'status': 'available'
# }
#
# headers = {
#     'accept': 'application/json',
#     'Content-Type': 'application/json'
#
# }
#
# data = {
#   "id": 0,
#   "username": "test.19",
#   "firstName": "test.20",
#   "lastName": "upsss",
#   "email": "test.19fff@mail.ru",
#   "password": "qwerty",
#   "phone": "84950850505",
#   "userStatus": 0
# }
#
# res = requests.post('https://petstore.swagger.io/v2/user', headers = headers, json=data)
#
# print(res.status_code)
# print(res.json())


# # GET-запрос: получить пользователя по имени пользователя
#
# status='available'
# res = requests.get( f"https://petstore.swagger.io/v2/user/test.19", headers = {'accept': 'application/json'})
#
#
# print(res.status_code)
# print(res.text)
# print(res.json())
# print(type(res.json()))


# PUT - запрос обновление данных ползователя
#
# params ={
#     'status': 'available'
# }
#
# headers = {
#     'accept': 'application/json',
#     'Content-Type': 'application/json'
#
# }
#
# data = {
#   "id": 0,
#   "username": "test.19",
#   "firstName": "test.20",
#   "lastName": "eee",
#   "email": "test.19fff@mail.ru",
#   "password": "qwerty",
#   "phone": "84950850505",
#   "userStatus": 0
# }
#
# res = requests.put('https://petstore.swagger.io/v2/user/test.19fff', headers = headers, json=data)
#
# print(res.status_code)
# print(res.json())
#
#DELETE - запрос: удалить пользователя
#
# status = 'available'
# res = requests.delete(f"https://petstore.swagger.io/v2/user/test.19", headers = {'accept': 'application/json'})
#
#
# print(res.status_code)
# print(res.json())















