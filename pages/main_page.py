import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_on_account_button(self):
        self.click_on_element_with_wait(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step("Нажать на кнопку 'Конструктор'")
    def click_on_constructor_button(self):
        self.click_on_element_with_wait(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажать на кнопку 'Лента заказов'")
    def click_on_order_feed_button(self):
        self.click_on_element_with_wait(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик на первый ингредиент")
    def click_on_first_ingredient(self):
        self.move_to_element_and_click(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Получить текст хедера в модальном окне 'Детали ингредиента'")
    def get_ingredient_modal_header_text(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_MODAL_HEADER)

    @allure.step("Клик на кнопку закрытия модального окна 'Детали ингредиента'")
    def click_to_cross_button_in_modal_window(self):
        self.click_on_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_MODAL)

    @allure.step("Найти форму модального окна на странице")
    def find_ingredient_modal_window(self):
        self.element_exist(MainPageLocators.INGREDIENT_DETAILS_MODAL_FORM)

    @allure.step("Получить данные счетчика ингредиента")
    def get_counter_value(self):
        self.wait_until_element_becomes_visible(MainPageLocators.INGREDIENT_COUNTER)
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Перетащить ингредиент в корзину")
    def drag_and_drop_ingredient_in_basket(self):
        self.drag_and_drop_element(MainPageLocators.FIRST_INGREDIENT, MainPageLocators.BURGER_BASKET)

    @allure.step("Клик на кнопку 'Оформить заказ'")
    def click_on_place_order_button(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Клик на кнопку закрытия модального окна оформленного заказа")
    def click_on_cross_button_in_success_modal_window(self):
        self.find_element_with_wait(MainPageLocators.CROSS_BUTTON_SUCCESS_ORDER_MODAL_WINDOW)
        self.click_on_element_using_script(MainPageLocators.CROSS_BUTTON_SUCCESS_ORDER_MODAL_WINDOW)
        self.wait_until_element_becomes_invisible(MainPageLocators.SUCCESS_ORDER_MODAL_WINDOW)

    @allure.step("Получить номер заказа в формате строки")
    def get_order_number_converted_to_string(self):
        self.find_element_with_wait(MainPageLocators.ORDER_NUMBER)
        return f'0{self.get_new_element_value(MainPageLocators.ORDER_NUMBER)}'

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        self.find_element_with_wait(MainPageLocators.ORDER_NUMBER)
        return self.get_new_element_value(MainPageLocators.ORDER_NUMBER)
