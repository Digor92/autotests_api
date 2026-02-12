from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str
    street: str
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias= "isActive")
    address: Address

user_data = User(id = 1,
            name = "Igor",
            email = "Igor@mail.ru",
            isActive = True,
            address = {"city":"Moscow", "street":"beet"})
            #Address(city = "Moscow", street = "beet"})
print(user_data) # это модель
print(type(user_data)) # тип модель
print(user_data.model_dump(), type(user_data.model_dump())) # из модели получили словарь
print(user_data.model_dump_json(), type(user_data.model_dump_json())) # из модели получили json

user_data_2 = {
            "id":2,
            "name":"Igor2",
            "email":"Igor2@mail.ru",
            "isActive": True,
            "address": {"city":"Moscow", "street":"beet"}
}

user_2 = User(**user_data_2)
print(user_2.model_dump())



