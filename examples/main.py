
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('Hello Github')

if __name__ == '__main__':
    print_hi('Igor')

import json
# преобразуем json строку в словарь
json_data = '''{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": ["Python", "QA Automation", "API Testing"],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}'''
parset_data = json.loads(json_data)
print(parset_data['courses'])

# словарь преобразуем в json строку
data_dict  = {
  "name": "Иван",
  "age": 30,
  "is_student": False,
    }
json_string = json.dumps(data_dict, indent = 4)
print(json_string, type(json_string))

# чтение json файла
with open("json_example.json", "r", encoding ="utf-8") as file:
    read_data = json.load(file)
    print(read_data, 'тип данных: ', type(read_data))

# запись словаря в json файл
with open('json_user.json', 'w', encoding ='utf-8') as file:
    json.dump(data_dict, file, indent = 4, ensure_ascii = False)