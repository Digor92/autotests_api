from clients.privat_http_builder import AuthenticationUserSchema
from clients.public_httpx_builder import get_public_http_client
from clients.users.privat_users_client import get_privat_users_client
from clients.users.public_users_client import get_public_user_client, PublicUsersClient
from tools.fakers import get_random_email
from clients.users.users_schema import CreateUserRequestSchema

# создаем пользователя
public_users_client = get_public_user_client()

create_user_request = CreateUserRequestSchema(
    email = get_random_email(),
    password="12345",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user: ', create_user_response)

# чуть длиннее но аналогично двум строкам выше

#create_user_response = public_users_client.create_user_api(create_user_request)
#create_user_response_data = create_user_response.json()
#print('Create user: ', create_user_response_data)

# аналогичный вызов только без билдера, мы сразу создаем экземпляр класса,
# передаем в него клиента и уже с работаем через методы экземпляра класса
# public_u_c = PublicUsersClient(get_public_http_client())
# create_u_r = public_u_c.create_user_api(create_user_request)
# create_u_r_d = create_u_r.json()
# print('Create user 2 : ', create_u_r_d)

# пользователь авторизуется
authentication_user = AuthenticationUserSchema(
    email = create_user_request.email,
    password = create_user_request.password

)
# получаем данные пользователя
private_users_client = get_privat_users_client(authentication_user)
get_user_response = private_users_client.get_user(create_user_response.user.id)
print('Get user data: ', get_user_response)
