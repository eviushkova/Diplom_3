import allure

import data


class TestMainPage:

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_open_constructor_page(self, main_page, login_page):
        main_page.click_on_constructor_button()
        expected_url = data.Url.BASE_URL
        current_url = main_page.get_current_url()

        assert current_url == expected_url

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_open_order_feed_page(self, main_page, login_page):
        main_page.click_on_order_feed_button()
        expected_url = data.Url.ORDER_FEED_URL
        current_url = main_page.get_current_url()

        assert current_url == expected_url

    @allure.title("Просмотр деталей ингредиента")
    def test_open_ingredient_details_modal_window(self, main_page):
        main_page.click_on_first_ingredient()
        main_page.get_ingredient_modal_header_text()
        expected_text = data.Data.HEADER_INGREDIENT_MODAL_TEXT
        current_text = main_page.get_ingredient_modal_header_text()

        assert current_text == expected_text

    @allure.title("Проверка закрывается всплывающего окна кликом по крестику")
    def test_close_ingredient_details_modal_window(self, main_page):
        main_page.click_on_first_ingredient()
        main_page.click_to_cross_button_in_modal_window()
        current_result = main_page.find_ingredient_modal_window()

        assert not current_result

    @allure.title("Проверка увеличения счетчика ингредиента при добавлении ингредиента в заказ")
    def test_add_ingredient_in_basket_and_check_ingredient_counter(self, main_page):
        main_page.drag_and_drop_ingredient_in_basket()
        counter = main_page.get_counter_value()

        assert counter == data.Data.INGREDIENT_QUANTITY

    @allure.title("Проверка успешного создания заказа залогиненным пользователем")
    def test_order_creation_by_authorized_user(self, authorization, main_page):
        main_page.drag_and_drop_ingredient_in_basket()
        main_page.click_on_place_order_button()
        order_status_text = main_page.get_order_status()

        assert order_status_text == data.Data.ORDER_STATUS_PREPARATION_MESSAGE
