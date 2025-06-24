import allure
import data
from locators.forgot_password_locators import ForgotPasswordLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Открыть страницу 'Логин'")
    def open_page(self):
        self.get_url(data.Url.LOGIN_URL)

    @allure.step("Ожидание загрузки страницы")
    def wait_until_page_load(self):
        self.wait_until_element_becomes_visible(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Нажать на ссылку 'Восстановить пароль'")
    def click_on_forgot_password_link(self):
        self.click_on_element_with_wait(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Заполнить поле 'email'")
    def fill_email(self, email):
        self.set_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Нажать на кнопку 'Восстановить'")
    def click_on_recovery_button(self):
        self.click_on_element_with_wait(ForgotPasswordLocators.RECOVERY_BUTTON)

    @allure.step("Ввести пароль")
    def fill_password(self, password):
        self.set_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Кликнуть на ссылку 'Зарегистрироваться'")
    def click_on_register_link(self):
        self.click_on_element(LoginPageLocators.REGISTER_LINK)

    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_on_sign_in_button(self):
        self.click_on_element_with_wait(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизация")
    def authorization(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_on_sign_in_button()
