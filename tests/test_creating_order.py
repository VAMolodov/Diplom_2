import requests
import pytest
import allure
from data import *


class TestCreateOrder:
    @allure.title('Проверка возможности создания заказа авторизированым пользователем с валидным хешем ингредиентов')
    def test_order_creation_with_authorization_whith_ingr (self,registered_and_del_create_user):
        auth_token = registered_and_del_create_user [1]
        headers = {'Authorization': auth_token }

        with allure.step('Отправляется запрос на создание заказа с валидным хешем ингредиентов'):
            create_order_with_auth_response = requests.post(Urls.url_create_order, headers=headers, json = Ingridients.ingr_payload)
            response_json = create_order_with_auth_response.json()

        assert response_json.get('success') == True
        assert 'number' in response_json.get('order')
        assert 'name' in response_json


    @allure.title('Проверка возможности создания заказа авторизированым пользователем без ингредиентов')
    def test_order_creation_with_authorization_whithout_ingr (self,registered_and_del_create_user):
        auth_token = registered_and_del_create_user [1]
        headers = {'Authorization': auth_token }

        with allure.step('Отправляется запрос на создание заказа без ингредиентов'):
            create_order_without_ingr_response = requests.post(Urls.url_create_order, headers=headers, json = Ingridients.not_ingr_payload)
            response_json = create_order_without_ingr_response.json()

        assert create_order_without_ingr_response.status_code == 400
        assert response_json.get('success') == False
        assert response_json.get('message') == "Ingredient ids must be provided"
    
    @allure.title('Проверка возможности создания заказа авторизированым пользователем с фейковым хешем ингредиентов')
    def test_order_creation_with_authorization_fake_ingr (self,registered_and_del_create_user):
        auth_token = registered_and_del_create_user [1]
        headers = {'Authorization': auth_token }

        with allure.step('Отправляется запрос на создание заказа с фейковым хешем ингредиентов'):
            create_order_with_auth_fake_ingr_response = requests.post(Urls.url_create_order, headers=headers, json = Ingridients.fake_ingr_payload)
            response_json = create_order_with_auth_fake_ingr_response.json()

        assert create_order_with_auth_fake_ingr_response.status_code == 500
        assert response_json.get('order') is None


    @allure.title('Проверка возможности создания заказа не авторизированым пользователем с валидным хешем ингредиентов')
    def test_order_creation_not_authorization_whith_ingr (self):
        headers = {'Authorization': ''}

        with allure.step('Отправляется запрос на создание заказане не авторизированым пользователем с валидным хешем ингредиентов'):
            create_order_not_auth_response = requests.post(Urls.url_create_order, headers=headers, json = Ingridients.ingr_payload)
            response_json = create_order_not_auth_response.json()

        assert response_json.get('success') == False
        assert 'number' not in response_json.get('order')
        assert 'name' not in response_json