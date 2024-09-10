import allure
import data
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Открыть страницу 'Лента заказов'")
    def open_order_feed_page(self):
        self.get_url(data.Url.ORDER_FEED_URL)

    @allure.step("Дождаться загрузки страницы")
    def wait_order_page_load(self):
        self.wait_until_element_becomes_invisible(OrderFeedPageLocators.ORDER_FEED_PAGE_LOADER)

    @allure.step("Клик на первую карточку в ленте заказов")
    def click_on_first_order_card(self):
        self.click_on_element_with_wait(OrderFeedPageLocators.FIRST_ORDER_CARD)

    @allure.step("Проверить детали заказа в модальном окне")
    def check_order_details_modal_window(self):
        return self.element_exist(OrderFeedPageLocators.OPENED_ORDER_CARD)

    @allure.step("Получить список заказов")
    def get_order_list_numbers(self):
        orders_numbers_elements = self.get_list_of_elements(OrderFeedPageLocators.ORDER_CARDS)
        order_numbers = [order_element.text for order_element in orders_numbers_elements]

        return order_numbers

    @allure.step("Получить значение счетчика 'Выполнено за всё время'")
    def get_counter_value_completed_for_all_time(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.COMPLETED_FOR_ALL_TIME_COUNTER))

    @allure.step("Получить значения счетчика 'Выполнено за сегодня'")
    def get_counter_value_completed_for_today(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.COMPLETED_FOR_TODAY_COUNTER))

    @allure.step("Получить номер заказа в счетчике 'В работе'")
    def get_counter_value_orders_in_progress(self):
        self.get_new_element_value_in_progress(OrderFeedPageLocators.ORDER_ID_IN_PROGRESS)
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_ID_IN_PROGRESS)
