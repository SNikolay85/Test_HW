import pytest
from worker import visit, unic_geo_id, search_queries, ApiYa

geo_logs = [
      {'visit1': ['Москва', 'Россия']},
      {'visit2': ['Дели', 'Индия']},
      {'visit3': ['Владимир', 'Россия']},
      {'visit4': ['Лиссабон', 'Португалия']},
      {'visit5': ['Париж', 'Франция']},
      {'visit6': ['Лиссабон', 'Португалия']},
      {'visit7': ['Тула', 'Россия']},
      {'visit8': ['Тула', 'Россия']},
      {'visit9': ['Курск', 'Россия']},
      {'visit10': ['Архангельск', 'Россия']},
    ]
geo_logs_true = [
      {'visit1': ['Москва', 'Россия']},
      {'visit3': ['Владимир', 'Россия']},
      {'visit7': ['Тула', 'Россия']},
      {'visit8': ['Тула', 'Россия']},
      {'visit9': ['Курск', 'Россия']},
      {'visit10': ['Архангельск', 'Россия']},
    ]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98,35]
      }
ids_true = [98, 35, 15, 213, 54, 119]

queries = [
  'смотреть сериалы онлайн',
  'новости спорта',
  'афиша кино',
  'курс доллара',
  'сериалы этим летом',
  'курс по питону',
  'сериалы про спорт'
]
dict_true = {3: '57 %', 2: '43 %'}

class TestVisit:
    @pytest.mark.parametrize(
        'in_list, out_list', [
            (geo_logs, geo_logs_true)
        ]
    )
    def test_visted(self, in_list, out_list):
        result = visit(in_list)
        assert result == out_list

class TestUnic:
    @pytest.mark.parametrize(
        'in_dict, out_list', [
            (ids, ids_true)
        ]
    )
    def test_unic(self, in_dict, out_list):
        result = unic_geo_id(in_dict)
        assert result == out_list

class TestSearch:
    @pytest.mark.parametrize(
        'in_list, out_dict', [
            (queries, dict_true)
        ]
    )
    def test_search(self, in_list, out_dict):
        result = search_queries(in_list)
        assert result == out_dict

token_YD = '********'
uploader = ApiYa(token_YD)

name_folders = ('new_folder1', 'new_folder2')

class TestApiYa:
    @pytest.mark.parametrize(
        'name_folder', name_folders
    )
    def test_folder(self, name_folder):
        result = uploader.get_folder(name_folder)
        assert result == 201, 'Folder not created or already exist'

    @pytest.mark.parametrize(
        'name_folder', name_folders
    )
    def test_folder_exist(self, name_folder):
        result = uploader.get_folder(name_folder)
        assert result == 409, 'Folder not exist yet'

    @pytest.mark.parametrize(
        'name_folder', name_folders
    )
    def test_name_folder(self, name_folder):
        result = uploader.folder_list(name_folder)['name']
        assert result == name_folder
