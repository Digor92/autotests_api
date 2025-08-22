from clients.courses.courses_client import get_course_client, CreateCoursesDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.privat_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_user_client, CreateUserRequestDict
from tools.fakers import get_random_email

# сначала создадим пользователя
public_user_client = get_public_user_client()
create_user_request = CreateUserRequestDict(
    email = get_random_email(),
    password="12345",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_user_client.create_user(create_user_request)
print('Create user: ', create_user_response)

authentication_user = AuthenticationUserDict(
    email = create_user_request["email"],
    password = create_user_request["password"]
)

# реализуем два клиента работы с файлами и создания курса
file_client = get_files_client(authentication_user)
course_client = get_course_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename="test1.png",
    directory="courses",
    upload_file="./testdata/files/test1.png")

create_file_response = file_client.create_file(create_file_request)
print('Create file data', create_file_response)

# теперь создаем курс
create_course_request = CreateCoursesDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)


