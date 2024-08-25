import allure
import requests
from stuff.pathways import Pathways

class Methods:
    @staticmethod
    @allure.step("Создать юзера")
    def user_create(payload):
        response = requests.post(Pathways.USER_CREATE, json = payload)
        return response

    @staticmethod
    @allure.step("Удалить юзера")
    def user_delete(payload):
        try:
            fetch_token = requests.post(Pathways.USER_LOGIN, json=payload)
            fetch_token.raise_for_status()
            user_access_token = fetch_token.json().get('accessToken')
            if user_access_token:
                headers = {
                    "Authorization": f"Bearer {user_access_token}"
                }
                requests.delete(Pathways.USER_MULTIPURPOSE, headers = headers)
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"Не смог удалить юзера: {e}")

    @staticmethod
    @allure.step("Залогиниться под юзером")
    def user_login(payload):
        response = requests.post(Pathways.USER_LOGIN, json=payload)
        return response

    @staticmethod
    @allure.step("Разлогиниться из юзера")
    def user_logout(payload):
        try:
            fetch_token = requests.post(Pathways.USER_LOGIN, json=payload)
            fetch_token.raise_for_status()
            user_refresh_token = fetch_token.json().get('refreshToken')
            if user_refresh_token:
                payload =  {
                    "token": f"{user_refresh_token}"
                }
                requests.post(Pathways.USER_LOGOUT, json=payload)
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"Не смог разлогиниться из юзера: {e}")

    @staticmethod
    @allure.step("Изменить данные юзера")
    def user_patch(payload, new_data):
        try:
            fetch_token = requests.post(Pathways.USER_LOGIN, json=payload)
            fetch_token.raise_for_status()
            user_access_token = fetch_token.json().get('accessToken')
            if user_access_token:
                headers = {
                    "Authorization": f"Bearer {user_access_token}"
                }
                response = requests.patch(Pathways.USER_MULTIPURPOSE, headers=headers, json=new_data)
                return response
        except (requests.exceptions.RequestException, KeyError) as e:
            print(f"Не смог обновить данные юзера: {e}")