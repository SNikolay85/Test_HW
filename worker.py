import requests

def visit(geo_logs):
    new_lst = []
    for geo_rus in geo_logs:
        for geo_r, g in geo_rus.items():
            if 'Россия' in g:
                new_lst.append(geo_rus)
    return new_lst

def unic_geo_id(ids):
    geo_id = []
    for g in ids.values():
        geo_id += g
    geo_set = set(geo_id)
    geo_id = list(geo_set)
    return geo_id

def search_queries(queries):
    qu = {}
    for result in queries:
        result = len(result.split(' '))
        if result not in qu.keys():
            qu[result] = 1
        else:
            qu[result] += 1
    for k, v in qu.items():
        qu[k] = f'{round(v * 100 / len(queries))} %'
    return qu

class ApiYa:
    host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        headers = {'Authorization': f'OAuth {self.token}'}
        return headers

    def get_folder(self, name_folder):
        uri = 'v1/disk/resources/'
        url = self.host + uri
        params = {'path': f'/{name_folder}'}
        response = requests.put(url, headers=self.get_headers(), params=params)
        return response.status_code

    def folder_list(self, name_folder):
        uri = 'v1/disk/resources/'
        url = self.host + uri
        params = {'path': f'/{name_folder}'}
        response = requests.get(url, headers=self.get_headers(), params=params).json()
        return response


