class Pathways:
    base_path = "https://stellarburgers.nomoreparties.site/api/"
    order_create = base_path + "orders"
    password_reset = base_path + "password-reset"
    user_create = base_path + "auth/register"
    user_login = base_path + "auth/login"
    user_logout = base_path + "auth/logout"
    token_refresh = base_path + "auth/token"
    user_multipurpose = base_path + "auth/user" #DELETE, PATCH, GET
    orders_fetch_all = base_path + "orders/all"
    orders_fetch_by_user = base_path + "orders"
