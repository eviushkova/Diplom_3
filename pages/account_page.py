import allure
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Ожидание загрузки страницы")
    def wait_until_account_page_load(self):
        self.wait_until_element_becomes_visible(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_on_account_button(self):
        self.click_on_element_with_wait(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step("Нажать на кнопку 'История заказов'")
    def click_on_order_history_button(self):
        self.click_on_element_with_wait(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Ожидание исчезновения элемента загрузки 'Истории заказов'")
    def wait_until_history_page_load(self):
        self.wait_until_element_becomes_invisible(AccountPageLocators.ORDER_HISTORY_LOADER)

    @allure.step("Нажать на кнопку 'Выход'")
    def click_on_logout_button(self):
        self.click_on_element_with_wait(AccountPageLocators.LOGOUT_BUTTON)

    def get_first_order_number(self):
        return self.get_list_of_elements(AccountPageLocators.USER_ORDERS)[0].text

