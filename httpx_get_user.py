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
# задаем заголовок авторизации и получаем данного пользователя
my_headers = {'Authorization':f'Bearer {login_user_response_data["token"]["accessToken"]}'}
get_user_response = httpx.get(f'http://localhost:8000/api/v1/users/{creat_user_response_data["user"]["id"]}', headers = my_headers)
get_user_response_data = get_user_response.json()
print("3 получили данные пользователя: ", get_user_response_data)
print("3 получили статус код: ", get_user_response.status_code)










