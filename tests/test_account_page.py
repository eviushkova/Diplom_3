import allure
import data


class TestAccountPage:
    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_open_personal_account(self, authorization, account_page):
        authorization.click_on_account_button()
        account_page.wait_until_account_page_load()
        expected_url = data.Url.ACCOUNT_PROFILE_URL
        current_url = account_page.get_current_url()

        assert current_url == expected_url

    @allure.title("Проверка перехода по клику на «История заказов»")
    def test_open_history_order(self, authorization, account_page):
        authorization.click_on_account_button()
        account_page.wait_until_account_page_load()
        account_page.wait_until_history_page_load()
        account_page.click_on_order_history_button()
        expected_url = data.Url.ORDER_HISTORY_URL
        current_url = account_page.get_current_url()

        assert current_url == expected_url

    @allure.title("Выход из аккаунта по клику на кнопку «Выход»")
    def test_click_on_logout(self, login_page, authorization, account_page):
        authorization.click_on_account_button()
        account_page.wait_until_account_page_load()
        account_page.click_on_logout_button()
        login_page.wait_until_page_load()
        expected_url = data.Url.LOGIN_URL
        current_url = account_page.get_current_url()

        assert current_url == expected_url
