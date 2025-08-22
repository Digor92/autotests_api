from api_client_create_course import create_course_response
from clients.courses.courses_client import get_course_client
from clients.exercises.excercises_client import get_excercise_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.privat_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_user_client, CreateUserRequestDict
from tools.fakers import get_random_email

# создаем клиента
public_users_client = get_public_user_client()
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)
# данные для авторизации
authentication_user = AuthenticationUserDict(
    email = create_user_request['email'],
    password = create_user_request['password']
)

files_client = get_files_client(authentication_user)
courses_client = get_course_client(authentication_user)
exercises_client = get_excercise_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/test1.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_exercise_request = CreateExerciseRequestDict(
    title="Exercise 1",
    courseId=create_course_response['course']['id'],
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)

create_exercise_response =  exercises_client.create_exercise(create_exercise_request)
print('Create excercise data: ', create_exercise_response)

