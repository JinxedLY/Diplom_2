import allure
import requests
from stuff.methods import Methods
from stuff.pathways import Pathways
from stuff.test_data import APIResponses, Ingredients

class TestFetchOrderAPI:
    @allure.title("Проверка возможности получить заказы пользователя с авторизацией")
    @allure.description("Создаем юзера, создаем заказ, запрашиваем список заказов")
    def test_fetch_order_with_auth_success(self, user_make):
        Methods.user_create(user_make)
        login_response = Methods.user_login(user_make)
        access_token = login_response.json().get('accessToken')
        headers = {
            "Authorization": access_token
        }
        body = {"ingredients":[Ingredients.BUN]}
        requests.post(Pathways.ORDER_CREATE, headers=headers, json=body)
        response = requests.get(Pathways.ORDERS_FETCH_BY_USER, headers=headers)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json.get("success") is True
        assert "total" in response_json
        assert "totalToday" in response_json
        assert "orders" in response_json

    @allure.title("Проверка невозможности получить заказы пользователя без авторизации")
    @allure.description("Создаем юзера, создаем заказ, в запросе на список заказов забываем токен")
    def test_fetch_order_without_auth_failure(self, user_make):
        Methods.user_create(user_make)
        login_response = Methods.user_login(user_make)
        access_token = login_response.json().get('accessToken')
        headers = {
            "Authorization": access_token
        }
        body = {"ingredients":[Ingredients.BUN]}
        requests.post(Pathways.ORDER_CREATE, headers=headers, json=body)
        response = requests.get(Pathways.ORDERS_FETCH_BY_USER)
        assert response.status_code == 401
        assert response.json() == APIResponses.USER_NO_AUTH