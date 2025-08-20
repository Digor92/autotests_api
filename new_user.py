
from clients.users.public_users_client import PublicUsersClient
from httpx import Client

base_client = Client(
    base_url="https://api.example.com",
    timeout=30
)


req = {
  "email": "user@example.com",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
new_user = PublicUsersClient(base_client)
print(new_user.create_user_api(req))