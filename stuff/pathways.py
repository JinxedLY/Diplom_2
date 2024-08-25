class Pathways:
    BASE_PATH = "https://stellarburgers.nomoreparties.site/api/"
    INGREDIENT_FETCH = BASE_PATH + "ingredients"
    ORDER_CREATE = BASE_PATH + "orders"
    PASSWORD_RESET = BASE_PATH + "password-reset"
    USER_CREATE = BASE_PATH + "auth/register"
    USER_LOGIN = BASE_PATH + "auth/login"
    USER_LOGOUT = BASE_PATH + "auth/logout"
    TOKEN_REFRESH = BASE_PATH + "auth/token"
    USER_MULTIPURPOSE = BASE_PATH + "auth/user"  # DELETE, PATCH, GET
    ORDERS_FETCH_BY_USER = BASE_PATH + "orders"