import pytest
import requests
from data import *
from methods.user_methods import UserCreate

@pytest.fixture
def del_create_user(): # данная фикстура не создает пользователя а предоставляет данные для создания 
                       # и потом после теста удаляет его по токену
    payload = UserCreate.generate_user_data()
    
    yield payload

    login_response_user = requests.post(Urls.url_Login_user, json=payload) 
    response_json = login_response_user.json()
    accessToken = response_json.get('accessToken')
    UserCreate.del_new_user(accessToken)
    
@pytest.fixture
def registered_and_del_create_user():# данная фикстура создает пользователя а потом после теста удаляет его по токену
    payload = UserCreate.generate_user_data()
    user_data = UserCreate.register_new_user(payload)
    success = user_data['success']
    accessToken = user_data['accessToken']
    refreshToken = user_data['refreshToken']

    yield payload,refreshToken,accessToken,success

    UserCreate.del_new_user(accessToken)