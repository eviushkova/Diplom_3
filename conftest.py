import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import data
from helpers.helpers import generate_user_data
from pages.account_page import AccountPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.reset_password_page import ResetPasswordPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-search-engine-choice-screen')
        driver = webdriver.Chrome(options=options)
        driver.get(data.Url.BASE_URL)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
        driver.get(data.Url.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    page.get_url(data.Url.LOGIN_URL)

    return page


@pytest.fixture()
def reset_password_page(driver):
    return ResetPasswordPage(driver)


@pytest.fixture()
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def create_user():
    user_data = generate_user_data()
    response = requests.post(data.Url.REGISTER_URL_API, json=user_data)
    access_token = response.json()["accessToken"]
    yield user_data["email"], user_data["password"], access_token

    requests.delete(data.Url.DELETE_URL_API, headers={"Authorization": f'{access_token}'})


@pytest.fixture()
def authorization(create_user, login_page, driver):
    email, password, _ = create_user
    login_page.authorization(email, password)

    return MainPage(driver)


@pytest.fixture()
def create_order(create_user):
    _, _, access_token = create_user

    ingredients_data = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6f",
            "61c0c5a71d1f82001bdaaa70"
        ]
    }

    requests.post(data.Url.ORDER_URL_API, headers={"Authorization": f'{access_token}'}, json=ingredients_data)
