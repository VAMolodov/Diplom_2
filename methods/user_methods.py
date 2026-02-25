import requests   
from faker import Faker
from data import Urls

#  генерирует данные пользователя через Faker
class UserCreate:
    def generate_user_data():
        fake = Faker()
        return {'email': fake.email(),'password': fake.password(),'name': fake.name()}
        
    def register_new_user(payload): # создает уникального пользователя
        response = requests.post(Urls.url_create_user, data=payload)
        success = response.json().get('success')
        accessToken = response.json().get('accessToken')
        refreshToken = response.json().get('refreshToken')
        payload = response.json().get('user')
        return {'success': success,'accessToken': accessToken, 'refreshToken': refreshToken, 'user': payload }
    
    def del_new_user (accessToken): # удаляет пользователя по токену
        headers = {'Authorization': accessToken}
        response = requests.delete(Urls.url_delete_user, headers=headers)
        return response

      