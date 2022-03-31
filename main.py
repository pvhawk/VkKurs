import time
import requests
# импортируем pprint для более комфортного вывода информации
from pprint import pprint





if __name__ == '__main__':
    with open('token.txt', 'r') as file_object:
        token = file_object.read().strip()

    URL = 'https://api.vk.com/method/users.get'
    params = {
        'user_id': '15440',
        'access_token': token,  # токен и версия api являются обязательными параметрами во всех запросах к vk
        'v': '5.131'
    }
    res = requests.get(URL, params=params)
    pprint(res.json())