import httpx

# залогинились
login_payload = {
    'email':'dedkov@mail.ru',
    'password':'12345'
}
# сделали запрос и получили токены
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json = login_payload)
login_response_data = login_response.json()
print('login response: ',login_response_data)
print('Status code: ',login_response.status_code)

# из полученных ранее данных берем рефреш_токен
refresh_payload = {
    'refreshToken':login_response_data['token']['refreshToken']
}

# делаем запрос на обновление по рефреш_токену
refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json = refresh_payload)
refresh_response_data = refresh_response.json()
# выводим этот рефреш_токен (как видим акксесс токен поменялся)
print('refresh response: ', refresh_response_data)
print('Status code: ', refresh_response.status_code)
