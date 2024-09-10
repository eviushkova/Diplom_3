import allure

import data


class TestPasswordRecovery:
    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_on_recovery_password_button(self, login_page):
        login_page.click_on_forgot_password_link()
        expected_url = data.Url.FORGOT_PASSWORD_URL
        current_url = login_page.get_current_url()

        assert current_url == expected_url

    @allure.title("Проверка ввода почты и клик по кнопке «Восстановить»")
    def test_fill_email_and_click_on_recovery_button(self, login_page, reset_password_page, forgot_password_page):
        login_page.click_on_forgot_password_link()
        forgot_password_page.fill_email(data.Data.EMAIL)
        forgot_password_page.click_on_recovery_button()
        reset_password_page.wait_until_page_load()
        expected_url = data.Url.RESET_PASSWORD_URL
        current_url = login_page.get_current_url()

        assert current_url == expected_url

    @allure.title("Проверка клик по кнопке показать/скрыть пароль делает поле активным")
    def test_click_on_show_password_button(self, login_page, reset_password_page, forgot_password_page):
        login_page.click_on_forgot_password_link()

        forgot_password_page.fill_email(data.Data.EMAIL)
        forgot_password_page.click_on_recovery_button()

        reset_password_page.wait_until_page_load()
        reset_password_page.fill_password(data.Data.PASSWORD)
        reset_password_page.click_on_show_password_icon()
        result = reset_password_page.return_password_value()

        assert result == data.Data.PASSWORD
