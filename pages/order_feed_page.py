import data
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def open_order_feed_page(self):
        self.get_url(data.Url.ORDER_FEED_URL)

    def wait_order_page_load(self):
        self.wait_until_element_becomes_invisible(OrderFeedPageLocators.ORDER_FEED_PAGE_LOADER)

    def click_on_first_order_card(self):
        self.click_on_element_with_wait(OrderFeedPageLocators.FIRST_ORDER_CARD)

    def check_order_details_modal_window(self):
        return self.element_exist(OrderFeedPageLocators.OPENED_ORDER_CARD)

    def get_order_list_numbers(self):
        orders_numbers_elements = self.get_list_of_elements(OrderFeedPageLocators.ORDER_CARDS)
        order_numbers = [order_element.text for order_element in orders_numbers_elements]

        return order_numbers

    def get_counter_value_completed_for_all_time(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.COMPLETED_FOR_ALL_TIME_COUNTER))

    def get_counter_value_completed_for_today(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.COMPLETED_FOR_TODAY_COUNTER))

    def get_counter_value_orders_in_progress(self):
        self.get_new_element_value_in_progress(OrderFeedPageLocators.ORDER_ID_IN_PROGRESS)
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_ID_IN_PROGRESS)

    # def get_order_in_progress(self):
    #     order_number_in_progress_element = self.get_element(OrderFeedPageLocators.ORDER_ID_IN_PROGRESS)
    #     order_number = [order_element.text for order_element in order_number_in_progress_element]
    #
    #     return order_number
