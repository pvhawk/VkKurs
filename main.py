import time
import requests
# импортируем pprint для более комфортного вывода информации
from pprint import pprint

if __name__ == '__main__':

    with open('token.txt', 'r') as file_object:
        token = file_object.read().strip()

    # URL = 'https://api.vk.com/method/users.get'
    # params = {
    #     'user_id': '15440',
    #     'access_token': token,  # токен и версия api являются обязательными параметрами во всех запросах к vk
    #     'v': '5.131'
    # }

    # URL = 'https://api.vk.com/method/photos.getAlbums'
    # params = {
    #     'owner_id': '1',
    #
    #     'access_token': token,  # токен и версия api являются обязательными параметрами во всех запросах к vk
    #     'v': '5.131',
    #     'count': '1',
    # }
    count_photo = 5
    URL = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': '254800',
        'album_id': 'profile',
        'access_token': token,  # токен и версия api являются обязательными параметрами во всех запросах к vk
        'v': '5.131',
        'count': str(count_photo),
        'extended': '1'
    }

    res = requests.get(URL, params=params)
    for photo in range(count_photo):
        pprint(res.json()['response']['items'][photo]['likes']['count'])
        pprint(res.json()['response']['items'][photo]['sizes'][-1])
    # pprint(res.json()['response']['items'][1]['sizes'][-1])
    # pprint(res.json()['response']['items'][2]['sizes'][-1])
    # pprint(res.json()['response']['items'][3]['sizes'][-1])
    # pprint(res.json()['response']['items'][4]['sizes'][-1])
