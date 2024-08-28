import allure
import pytest
import requests

from stuff.methods import Methods
from stuff.pathways import Pathways
from stuff.test_data import APIResponses

class TestPatchUserAPI:
    @pytest.mark.parametrize("altered_field", ["email", "name"])
    @allure.title("Проверка возможности изменения данных пользователя")
    @allure.description("Создаем юзера, меняем поле, смотрим на результат")
    def test_patch_user_with_authorisation_success(self, user_make, altered_field):
        Methods.user_create(user_make)
        login_response = Methods.user_login(user_make)
        access_token = login_response.json().get('accessToken')
        headers = {
            "Authorization": access_token
        }
        altered_payload = user_make.copy()
        existing_value = altered_payload[altered_field]
        new_value = existing_value + "12"
        altered_payload[altered_field] = new_value
        user_patch = requests.patch(Pathways.USER_MULTIPURPOSE, json=altered_payload, headers=headers)
        assert user_patch.status_code == 200
        updated_user_data = user_patch.json().get("user")
        assert updated_user_data[altered_field] == new_value
        Methods.user_delete(altered_payload)

    @pytest.mark.parametrize("altered_field", ["email", "name"])
    @allure.title("Проверка невозможности изменения данных пользователя без авторизации")
    @allure.description("Создаем юзера, меняем поле, забываем передать токен, смотрим на результат")
    def test_patch_user_without_authorisation_failure(self, user_make, altered_field):
        Methods.user_create(user_make)
        altered_payload = user_make.copy()
        existing_value = altered_payload[altered_field]
        new_value = existing_value + "12"
        altered_payload[altered_field] = new_value
        user_patch = requests.patch(Pathways.USER_MULTIPURPOSE, json=altered_payload)
        assert user_patch.status_code == 401
        assert user_patch.json() == APIResponses.USER_NO_AUTH
