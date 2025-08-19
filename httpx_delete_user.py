import httpx
from tools.fakers import get_random_email
# создаем пользователя
creat_user_payload = {
    "email": get_random_email(),
    "password": "12345",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

creat_user_response = httpx.post('http://localhost:8000/api/v1/users', json = creat_user_payload)
creat_user_response_data = creat_user_response.json()
print('1 пользователь создался:', creat_user_response_data)

# авторизуемся с созданным пользователем
login_payload = { 'email':creat_user_payload['email'],
                  'password':creat_user_payload['password']
}
login_user_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json = login_payload)
login_user_response_data = login_user_response.json()
print("2 пользователь авторизовался: ", login_user_response_data)

# удаляем пользователя
my_headers = {'Authorization':f'Bearer {login_user_response_data["token"]["accessToken"]}'}
delete_user_response = httpx.delete(f'http://localhost:8000/api/v1/users/{creat_user_response_data["user"]["id"]}', headers = my_headers)
print('3 статус код при удалении пользователя: ', delete_user_response.status_code)
