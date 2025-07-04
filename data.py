class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"

    REGISTER_ENDPOINT_API = "api/auth/register"
    DELETE_ENDPOINT_API = "api/auth/user"
    LOGIN_ENDPOINT_API = "api/auth/login"
    LOGIN_ENDPOINT = "login"
    FORGOT_PASSWORD_ENDPOINT = "forgot-password"
    RESET_PASSWORD_ENDPOINT = "reset-password"
    ACCOUNT_PROFILE_ENDPOINT = "account/profile"
    ORDER_HISTORY_ENDPOINT = "account/order-history"
    ORDER_FEED_ENDPOINT = "feed"
    ORDER_ENDPOINT_API = "api/orders"

    REGISTER_URL_API = f'{BASE_URL}{REGISTER_ENDPOINT_API}'
    LOGIN_URL_API = f'{BASE_URL}{LOGIN_ENDPOINT_API}'
    DELETE_URL_API = f'{BASE_URL}{DELETE_ENDPOINT_API}'
    LOGIN_URL = f'{BASE_URL}{LOGIN_ENDPOINT}'
    FORGOT_PASSWORD_URL = f'{BASE_URL}{FORGOT_PASSWORD_ENDPOINT}'
    RESET_PASSWORD_URL = f'{BASE_URL}{RESET_PASSWORD_ENDPOINT}'
    ACCOUNT_PROFILE_URL = f'{BASE_URL}{ACCOUNT_PROFILE_ENDPOINT}'
    ORDER_HISTORY_URL = f'{BASE_URL}{ORDER_HISTORY_ENDPOINT}'
    ORDER_FEED_URL = f'{BASE_URL}{ORDER_FEED_ENDPOINT}'
    ORDER_URL_API = f'{BASE_URL}{ORDER_ENDPOINT_API}'


class Data:
    EMAIL = "mario@testino.ru"
    PASSWORD = "1111"
    HEADER_INGREDIENT_MODAL_TEXT = "Детали ингредиента"
    INGREDIENT_QUANTITY = '2'
    ORDER_STATUS_PREPARATION_MESSAGE = "Ваш заказ начали готовить"
    BASE_ORDER_ID = '9999'
    BASE_ORDER_IN_PROGRESS_STATUS = "Все текущие заказы готовы!"
