import allure

from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step("Заполнить поле 'email'")
    def fill_email(self, email):
        self.set_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Нажать на кнопку 'Восстановить'")
    def click_on_recovery_button(self):
        self.click_on_element_with_wait(ForgotPasswordLocators.RECOVERY_BUTTON)
