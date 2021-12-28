import requests, os
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        HEADERS = {"Authorization" : f'OAuth {self.token}'}
        params = {'path': path_to_file, 'overwrite':"true"}
        response = requests.get(upload_url, headers=HEADERS, params=params)
        pprint(response.status_code)
        return response.json()

    def upload_file_to_disk(self, path_to_file, filename):
        href = self.upload(path_to_file= path_to_file).get('href','')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.normpath('text.txt')
    token = ' '
    uploader = YaUploader(token=token)
    result = uploader.upload_file_to_disk(path_to_file, "text.txt")
