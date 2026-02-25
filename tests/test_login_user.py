import requests
import pytest
import allure
from methods.user_methods import UserCreate
from data import *

class TestLoginUser:

    @allure.title('Проверка входа под существующим пользователем ')
    @allure.description('Пользователь создается с генерируемыми Faker данными,'
                        'после пробуем авторизоваться с теми же данными '
                        'после пользатель удаляется из БД после теста')
    
    def test_login_under_an_existing_user(self, registered_and_del_create_user):
        payload = registered_and_del_create_user [0]

        with allure.step('Отправляется запрос на авторизацию пользователя в приложения с теми же данными'):
            login_response = requests.post(Urls.url_Login_user, json = payload)
            response_json = login_response.json()

             
        assert login_response.status_code == 200
        assert response_json.get('success') == True
        assert response_json.get('accessToken') is not None
        assert response_json.get('refreshToken') is not None
        assert response_json.get('user') is not None



    @allure.title('Проверка возможности входа пользователя с несуществующими парой логин/пароль')
    def test_log_in_with_incorrect_username_and_password(self):
        fake_payload = UserCreate.generate_user_data()
        with allure.step('Отправляется запрос на вход пользователя в приложения с несуществующими парой логин/пароль'):     
            fake_response = requests.post(Urls.url_Login_user, json = fake_payload)
            response_json = fake_response.json()

        assert fake_response.status_code == 401
        assert response_json.get('success') == False
        assert response_json.get('message') == 'email or password are incorrect'

