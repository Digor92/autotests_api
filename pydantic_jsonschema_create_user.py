from clients.authentication.authentication_schema import TokenSchema
from tools.assertions.schema import validate_json_schema

print(TokenSchema.model_json_schema())
#сгенерированная json схема
# schema = {'properties':
#               {'tokenType':
#                    {'title': 'Tokentype', 'type': 'string'},
#                     'accessToken': {'title': 'Accesstoken', 'type': 'string'},
#                     'refreshToken': {'title': 'Refreshtoken', 'type': 'string'}
#                },
#           'required': ['tokenType', 'accessToken', 'refreshToken'],
#           'title': 'TokenSchema',
#           'type': 'object'
#           }
from clients.privat_http_builder import AuthenticationUserSchema
from clients.public_httpx_builder import get_public_http_client
from clients.users.privat_users_client import get_privat_users_client
from clients.users.public_users_client import get_public_user_client, PublicUsersClient
from tools.fakers import get_random_email
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
import jsonschema

public_users_client = get_public_user_client()

create_user_request = CreateUserRequestSchema(
    email = get_random_email(),
    password="12345",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user_api(create_user_request)
Create_user_response_schema = CreateUserResponseSchema.model_json_schema()
print(Create_user_response_schema)
print(create_user_response.json())

jsonschema.validate(instance=create_user_response.json(), schema=Create_user_response_schema)
validate_json_schema(instance=create_user_response.json(), schema=Create_user_response_schema)