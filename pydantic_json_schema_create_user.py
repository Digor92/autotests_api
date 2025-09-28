from clients.authentication.authentication_schema import TokenSchema
# from pydantic.json_schema import model_json_schema
#
# pr = model_json_schema(TokenSchema)
# print(pr)
# print(TokenSchema.model_json_schema())


from clients.users.public_users_client import get_public_user_client

from tools.assertions.schema import validate_json_schema
from tools.fakers import fake
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
import jsonschema

# создаем пользователя
public_users_client = get_public_user_client()

create_user_request = CreateUserRequestSchema(
    email = fake.email(),
    password="12345",
    last_name="string",
    first_name="string",
    middle_name="string"
)
# фактический результат
create_user_response = public_users_client.create_user_api(create_user_request)
# ожидаемый результат
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
# сгенерируем негативный кейс, уберем обязательное поле
#create_user_response_json = create_user_response.json()
#del create_user_response_json['user']['email']

jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_schema)
validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)



