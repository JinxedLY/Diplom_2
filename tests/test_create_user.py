import allure
import pytest
from stuff.methods import Methods
from stuff.test_data import APIResponses
from stuff.helpers import RealHumans

class TestUserCreateAPI:
    @allure.title("Проверка успешного создания юзера с рандомным набором данных")
    @allure.description("Тест создает нового юзера, используя рандомный набор данных, пост-фактум удаляет юзера")
    def test_create_new_user_random_data_success(self, user_make):
        user = Methods.user_create(user_make)
        assert user.status_code == 200
        user_data = user.json()
        assert user_data.get('success')
        assert "accessToken" in user_data
        assert "refreshToken" in user_data
        assert "user" in user_data

    @allure.title("Проверка невозможности создания второго юзера используя данные существующего юзера")
    @allure.description("Тест создает юзера, повторяет создание юзера. Пост-фактум удаляет юзера")
    def test_create_duplicate_user_duplicate_data_failure(self, user_make):
        Methods.user_create(user_make)
        user = Methods.user_create(user_make)
        assert user.status_code == 403
        assert user.json() == APIResponses.USER_DUPLICATE

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    @allure.title("Проверка невозможности создания юзера без передачи обязательного поля")
    @allure.description("Пытаемся создать юзера, но не передаем одно из обязательных полей")
    def test_create_user_without_data_failure(self, missing_field):
        payload = RealHumans.create_real_human()
        del payload[missing_field]
        user = Methods.user_create(payload)
        assert user.status_code == 403
        assert user.json() == APIResponses.USER_MISSING
