from clients.courses.courses_client import get_course_client
from clients.courses.courses_schema import CreateCoursesRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.privat_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_user_client
#from tools.fakers import fake
from clients.users.users_schema import CreateUserRequestSchema

# сначала создадим пользователя
public_user_client = get_public_user_client()
create_user_request = CreateUserRequestSchema(
    # email = fake.email(),
    # password="12345",
    # last_name="string",
    # first_name="string",
    # middle_name="string"
)
create_user_response = public_user_client.create_user(create_user_request)
print('Create user: ', create_user_response)

authentication_user = AuthenticationUserSchema(
    email = create_user_request.email,
    password = create_user_request.password
)
print(authentication_user)

# реализуем два клиента работы с файлами и создания курса
file_client = get_files_client(authentication_user)
course_client = get_course_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestSchema(
    #filename="test1.png",
    #directory="courses",
    upload_file="./testdata/files/testQA.png")

create_file_response = file_client.create_file(create_file_request)
print('Create fil'
      'marrie data', create_file_response)

# теперь создаем курс
create_course_request = CreateCoursesRequestSchema(
    #title="Python",
    #maxScore=100,
    #minScore=10,
    #description="Python API course",
    #estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)
create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)
