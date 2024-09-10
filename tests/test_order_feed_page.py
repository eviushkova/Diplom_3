import allure


class TestOrderFeedPage:
    @allure.title("Проверка открытия всплывающего окна с деталями заказа")
    def test_open_order_details_modal_window(self, order_feed_page):
        order_feed_page.open_order_feed_page()
        order_feed_page.click_on_first_order_card()
        current_result = order_feed_page.check_order_details_modal_window()

        assert current_result is True

    @allure.title("Проверка отображения существующего заказа из истории пользователя в «Ленте заказов»")
    def test_display_user_order_in_order_feed(self, create_order, authorization, main_page, account_page,
                                              order_feed_page):
        authorization.click_on_account_button()
        account_page.wait_until_account_page_load()
        account_page.wait_until_history_page_load()
        account_page.click_on_order_history_button()
        order_number = account_page.get_first_order_number()
        order_feed_page.open_order_feed_page()
        orders_feed = order_feed_page.get_order_list_numbers()

        assert order_number in orders_feed

    @allure.title("Проверка увеличения счетчика «Выполнено за всё время» при создании нового заказа")
    def test_counter_value_completed_for_all_time_increments(self, order_feed_page, main_page, authorization):
        main_page.click_on_order_feed_button()
        order_feed_page.wait_order_page_load()
        counter_value_before = order_feed_page.get_counter_value_completed_for_all_time()
        main_page.click_on_constructor_button()
        main_page.drag_and_drop_ingredient_in_basket()
        main_page.click_on_place_order_button()
        main_page.click_on_cross_button_in_success_modal_window()
        main_page.click_on_order_feed_button()
        order_feed_page.wait_order_page_load()
        counter_value_after = order_feed_page.get_counter_value_completed_for_all_time()

        assert counter_value_after > counter_value_before

    @allure.title("Проверка увеличения счетчика «Выполнено за всё сегодня» при создании нового заказа")
    def test_counter_value_completed_for_today_increments(self, order_feed_page, main_page, authorization):
        main_page.click_on_order_feed_button()
        order_feed_page.wait_order_page_load()
        counter_value_before = order_feed_page.get_counter_value_completed_for_today()
        main_page.click_on_constructor_button()
        main_page.drag_and_drop_ingredient_in_basket()
        main_page.click_on_place_order_button()
        main_page.click_on_cross_button_in_success_modal_window()
        main_page.click_on_order_feed_button()
        order_feed_page.wait_order_page_load()
        counter_value_after = order_feed_page.get_counter_value_completed_for_today()

        assert counter_value_after > counter_value_before

    @allure.title("Проверка увеличения счетчика «В работе» при создании нового заказа")
    def test_counter_value_in_progress_increments(self, authorization, main_page, order_feed_page):
        main_page.drag_and_drop_ingredient_in_basket()
        main_page.click_on_place_order_button()
        order_number = main_page.get_order_number()
        main_page.click_on_cross_button_in_success_modal_window()
        main_page.click_on_order_feed_button()
        order_feed_page.wait_order_page_load()
        order_number_in_progress_counter = order_feed_page.get_counter_value_orders_in_progress()

        assert order_number == order_number_in_progress_counter



