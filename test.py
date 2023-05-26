import requests

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status=available', headers={'accept':'application/json'})

print('Находим питомцев, статус код:', res.status_code)
print(res.text)
print(res.json())


headers={'accept':'application/json','Content-type':'application/json'}
data={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res1 = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, json=data)
print('Добавление нового питомца, статус код:', res1.status_code)
print(res1.text)
print(res1.json())


headers = {'accept':'application/json'}
res2 = requests.delete(f'https://petstore.swagger.io/v2/pet/9223372036854748996', headers=headers)

print('Удаление питомца, статус код:', res2.status_code)
print(res2.text)
print(res2.json())

headers = {'accept':'application/json','Content-type':'application/json'}
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res3 = requests.put(f'https://petstore.swagger.io/v2/pet', headers=headers, json=data)
print('Изменение данных питомца, статус код:', res3.status_code)
print(res3.text)
print(res3.json())



