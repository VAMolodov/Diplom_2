

class Urls:
    url_main = 'https://stellarburgers.nomoreparties.site' # адрес главной страницы
    url_create_user = f'{url_main}/api/auth/register' # эндпоинт для регистрации пользователя.
    url_Login_user = f'{url_main}/api/auth/login' # эндпоинт для авторизации
    url_Login_out_user = f'{url_main}/api/auth/logout' # эндпоинт для выхода из системы.
    url_delete_user = f'{url_main}/api/auth/user' # эндпоинт удаления пользователя.

    url_create_order = f'{url_main}/api/orders' # эндпоинт создания заказа.


class Ingridients:

    ingr_payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]} # валидный хеш ингридиентов
    not_ingr_payload = {"ingredients": [ ]} # без ингредиентов
    fake_ingr_payload = {"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]} # не валидный хеш ингридиентов