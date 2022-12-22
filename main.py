import requests
from pprint import pprint
from _datetime import datetime

TOKEN = ''
class Marvel():

    hero_book = []
    def _load_heroes_info(self):
        url = 'https://akabab.github.io/superhero-api/api'
        params = '/all.json'
        resp = requests.get(f'{url}/{params}')
        info = resp.json()
        return  info

    def add_hero_info(self, name):
        info = self._load_heroes_info()
        hero = [hero for hero in info if name == hero["name"]]
        for attr in hero:
             self.hero_book.append({'name': attr['name'], 'intelligence': attr['powerstats']['intelligence']})
        return

    def sorted_hero(self):
        smart_hero = {'name': '', 'intelligence': 0}
        for value in self.hero_book:
            if int(value['intelligence']) > int(smart_hero['intelligence']):
                smart_hero = value
        print(f"Самый умный герой из выбранных для сравнения {smart_hero['name']}")
        return



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_url(self, path):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': 'true'}
        responce = requests.get(files_url, headers=headers, params=params)
        return responce.json()
    def upload(self, path, filename):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        href = self._get_upload_url(path).get('href')
        print(href)
        headers = self.get_headers()
        responce = requests.put(href, data=open(filename, 'rb'))
        return


class Stack_Overflow():

    def python_qvest(self, fromdate, todate, tag):
        files_url = 'https://api.stackexchange.com/search?'
        headers = {'Accept-Encoding': 'gzip'}
        params = {'fromdate': int(datetime.strptime(fromdate, '%d.%m.%Y %H:%M').timestamp()), 'todate': int(datetime.strptime(todate, '%d.%m.%Y %H:%M').timestamp()),\
                 'order': 'desc', 'sort': 'activity', 'tagged': tag, 'site': 'stackoverflow'}
        responce = requests.get(files_url, headers=headers, params=params)
        pprint(responce.json())
        return

if __name__ == '__main__':

    ya = YaUploader(TOKEN)
    ya.upload('WORK.UDB', '\YA\WORK.UDB')

    heroes = Marvel()
    heroes.add_hero_info('Thanos')
    heroes.add_hero_info('Captain America')
    heroes.add_hero_info('Hulk')
    heroes.sorted_hero()

    st = Stack_Overflow()
    st.python_qvest('20.12.2022 00:00', '22.12.2022 00:00', 'Python')