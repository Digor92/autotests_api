import httpx
#from httpx import *
# Проходим аутентификацию
login_payload = {
    "email": "dedkov@mail.ru",
    "password": "12345"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

client = httpx.Client(base_url = "http://localhost:8000",
                      timeout = 100,
                      headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
                      )

get_user_me_response = client.get('/api/v1/users/me')
get_user_me_response_data = get_user_me_response.json()
print("get user me data: ", get_user_me_response_data)