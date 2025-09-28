# из бибилиотеки faker импортировали класс Faker
from faker import Faker
import requests
import httpx

#import faker
#fake = faker.Fake()

# создали экземпляр класса
fake = Faker('ru_RU')
user_data = {
    "name":fake.name(),
    "email":fake.email(),
    "age":fake.random_int(min=18,max=100)
}
print(user_data)

