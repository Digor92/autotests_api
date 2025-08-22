import httpx

response1 = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
print(response1, type(response1))
print(response1.status_code)
print(response1.json())

data2 = {
    'userId':1,
    'title': 'new example',
    'complited':True,
}

response2 = httpx.post('https://jsonplaceholder.typicode.com/todos', json = data2)
print(response2.status_code)
print(response2.json())

data3 = {'username':'test_user', 'password': '12345'}
response3 = httpx.post('https://httpbin.org/post', data = data3)
print(response3.status_code)
#print(response3.request.headers)
print(response3.json())

headers4 = {'Autorisation':'my bearer token castom'}
response4 = httpx.get('https://httpbin.org/get', headers = headers4)
print(response4.status_code)
print(response4.json())
print(response4.request.headers)

params5 = {'userId':1}
response5 = httpx.get('https://jsonplaceholder.typicode.com/todos', params = params5)
print(response5.url)
#print(response5.json())

# работа с файлами
files6 = {"file": ('example.txt', open('example.txt', 'rb'))}
response6 = httpx.post('https://httpbin.org/post', files = files6)
print('работа с файлами:  \n',response6.json())

# работа с сессиями
# когда у нас открылось соединение мы передаем несколько запросов
# для этого используем класс Client
with httpx.Client() as client:
    response7_1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
    response7_2 = client.get('https://jsonplaceholder.typicode.com/todos/2')
print(response7_1.json())
print(response7_2.json())

# передача заголовков на уровне клиента чтобы во всех запросах их не прописывать и они использовались
client = httpx.Client(headers = {'Autorisation':'my bearer token castom'})
response8 = client.get('https://httpbin.org/get')
print('response8: \n', response8.json())
client.close()

# работа с ошибками
try:
    response9 = httpx.get('https://jsonplaceholder.typicode.com/no_valid')
    # поднимаем ошибку если статус код неуспешен
    response9.raise_for_status()
    #print(response9.status_code)
except httpx.HTTPStatusError as e:
    print(f'ОШИБКА {e}')

try:
    response9 = httpx.get('https://httpbin.org/get', timeout=2)
    print(response9.status_code)
except httpx.ReadTimeout as r:
    print(f'Долгое ожидание: {r}')



