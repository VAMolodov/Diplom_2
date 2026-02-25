import requests
import pytest
import allure
from methods.user_methods import UserCreate
from data import *

class TestUserReg:
    @allure.title('Проверка регистрации уникального пользователя ')
    @allure.description('Пользователь создается с генерируемыми Faker данными и удаляется из БД после теста')
    def test_create_unique_user(self, del_create_user):
        payload = del_create_user
        with allure.step('Создается уникальный пользователь'):
            create_unique_user = UserCreate.register_new_user(payload) 

        assert create_unique_user['success'] == True
        assert create_unique_user['accessToken'] is not None
        assert create_unique_user['refreshToken'] is not None
        assert create_unique_user['user'] is not None

    @allure.title('Проверка регистрации пользователя который уже зарегистрирован ')
    def test_create_user_already_registered(self, registered_and_del_create_user):
        payload = registered_and_del_create_user [0] 
        with allure.step('Отправляется повторный запрос на создание пользователя с теми же данными'):
            repeat_response = requests.post(Urls.url_create_user, json = payload)
            response_json = repeat_response.json()

        assert repeat_response.status_code == 403 
        assert response_json.get('success') == False
        assert response_json.get('message') == 'User already exists'

    @allure.title('Проверка возможности регистрации пользователя который без заполнения одно из обязательных полей')
    @allure.description('выполняем три теста: по очереди отправляем запросы, где не заполнено одно из полей — email, passwdord или name')
    
    @pytest.mark.parametrize('empty_data',
                            [{'email': '', 'password': UserCreate.generate_user_data()['password'], 'name': UserCreate.generate_user_data()['name'] },
                            {'email': UserCreate.generate_user_data()['email'], 'password': '', 'name': UserCreate.generate_user_data()['name']},
                            {'email': UserCreate.generate_user_data()['email'], 'password': UserCreate.generate_user_data()['password'], 'name': ''}])
    
    def test_create_user_whiout_required_fields(self,empty_data):
        with allure.step('Отправляется запрос на создание пользователя без какого либо заполненного поля'):
            response = requests.post(Urls.url_create_user, json = empty_data)
            response_json = response.json()

        assert response.status_code == 403
        assert response_json.get('success') == False
        assert response_json.get('message') == 'Email, password and name are required fields' 