from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient

class NewUsersDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    def create_user_api(self, request: NewUsersDict)->Response:
        return self.post('/api/v1/users', json = request)

