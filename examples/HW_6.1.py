import httpx

login_payload = {
    'email':'dedkov@mail.ru',
    'password':'12345'
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json = login_payload)
login_response_data = login_response.json()

my_headers = {'Authorization':f"Bearer {login_response_data['token']['accessToken']}"
           }
get_user_response = httpx.get( 'http://localhost:8000/api/v1/users/me', headers = my_headers)
get_user_response_data = get_user_response.json()

print(get_user_response.status_code)
print(get_user_response_data)


