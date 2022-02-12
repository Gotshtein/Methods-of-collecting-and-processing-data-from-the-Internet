import requests
import json
url = 'https://api.github.com'
user='Plotojadnij'
r = requests.get(f'{url}/users/{user}/repos')
data = json.loads(r.text)
lenght = len(data)
print('Список репозиториев пользователя:')
for i in range(lenght):
    print('- ', data[i]['name'])
# Список репозиториев пользователя:
# Math_Basic
#  MySql
#  Python-for-Data-Science
#  Python1
#  Test
# Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл. ###

url = 'https://api.vk.com/method/status.get?v=5.52&access_token='
token = '9b6320419176b03a464becbc1da17775490c35cb01f278bd79eb80ce3e0cc285ed50988d820aa098fcb6c'
# Statusstatus.get

# Получает текст статуса пользователя или сообщества. Этот метод можно вызвать с ключом доступа пользователя. Требуются права доступа: status.

r = requests.get(f'{url}{token}')
data = json.loads(r.text)

file = open('user_status.txt', 'w')
file.write(r.text)
file.close()