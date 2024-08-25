import allure
import requests
from stuff.methods import Methods
from stuff.pathways import Pathways
from stuff.test_data import APIResponses, Ingredients

class TestCreateOrderAPI:
    @allure.title("Проверка возможности создания заказа с авторизацией")
    @allure.description("Создаем юзера, создаем заказ, радуемся")
    def test_create_order_with_just_buns_with_auth_success(self, user_make):
        Methods.user_create(user_make)
        login_response = Methods.user_login(user_make)
        access_token = login_response.json().get('accessToken')
        headers = {
            "Authorization": access_token
        }
        body = {"ingredients":[Ingredients.BUN]}
        response = requests.post(Pathways.ORDER_CREATE, headers=headers, json=body)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json.get("success") is True
        assert "name" in response_json
        assert "order" in response_json

    @allure.title("Проверка невозможности создания заказа без авторизации")
    @allure.description("Создаем заказ без создания юзера")
    def test_create_order_valid_ingredients_without_auth_success(self):
        body = {"ingredients":[Ingredients.BUN]}
        response = requests.post(Pathways.ORDER_CREATE, json=body)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json.get("success") is True
        assert "name" in response_json
        assert "order" in response_json

    @allure.title("Проверка возможности создания заказа с добавленными ингридиентами")
    @allure.description("Cоздаем заказ с мясом и соусом, радуемся")
    def test_create_order_valid_ingredients_success(self, user_make):
        body = {"ingredients": [Ingredients.BUN, Ingredients.MEAT, Ingredients.SAUCE]}
        response = requests.post(Pathways.ORDER_CREATE, json=body)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json.get("success") is True
        assert "name" in response_json
        assert "order" in response_json

    @allure.title("Проверка невозможности создания заказа без индигриентов")
    @allure.description("Cоздаем заказ без передачи индигриентов")
    def test_create_order_no_ingredients_failure(self, user_make):
        response = requests.post(Pathways.ORDER_CREATE)
        assert response.status_code == 400
        assert response.json() == APIResponses.NO_INGREDIENTS

    @allure.title("Проверка невозможности создания заказа с неверными хешами индигриентов")
    @allure.description("Cоздаем заказ с рандомными данными в индигриентах")
    def test_create_order_malformed_ingredients_failure(self, user_make):
        body = {"ingredients": ["notahash"]}
        response = requests.post(Pathways.ORDER_CREATE, json=body)
        assert response.status_code == 500

