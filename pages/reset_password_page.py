import allure
from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step("Ожидание загрузки страницы")
    def wait_until_page_load(self):
        self.wait_until_element_becomes_visible(ResetPasswordLocators.SHOW_PASSWORD_ICON)

    @allure.step("Ввести пароль")
    def fill_password(self, password):
        self.set_text_to_element(ResetPasswordLocators.PASSWORD_INPUT, password)

    @allure.step("Кликнуть на иконку 'показать пароль'")
    def click_on_show_password_icon(self):
        self.click_on_element_using_script(ResetPasswordLocators.SHOW_PASSWORD_ICON)

    # reset-password
    @allure.step("Вернуть значение поля 'показать пароль'")
    def return_password_value(self):
        password = self.get_attribute_value(ResetPasswordLocators.PASSWORD_INPUT, 'value')

        return password
