import allure
import pytest
from stuff.methods import Methods
from stuff.test_data import APIResponses

class TestUserLoginAPI:
    @allure.title("Проверка возможности логина с валидными данными")
    @allure.description("Создаем юзера, логинимся под этим юзером")
    def test_courier_login_valid_data_success(self, user_make):
        Methods.user_create(user_make)
        user_login = Methods.user_login(user_make)
        assert user_login.status_code == 200
        user_data = user_login.json()
        assert user_data.get('success')
        assert "accessToken" in user_data
        assert "refreshToken" in user_data
        assert "user" in user_data

    @pytest.mark.parametrize("altered_field", ["password", "email"])
    @allure.title("Проверка невозможности логина при некорректно переданном значении пароля или мыла")
    @allure.description("Создаем юзера, подменяем данные на другое значение, логинимся и ожидаем провал")
    def test_user_login_malformed_data_failure(self, altered_field, user_make):
        Methods.user_create(user_make)
        altered_payload = user_make.copy()
        existing_value = altered_payload[altered_field]
        new_value = existing_value + "12"
        altered_payload[altered_field] = new_value
        user_login = Methods.user_login(altered_payload)
        assert user_login.status_code == 401
        assert user_login.json() == APIResponses.USER_MALFORMED
