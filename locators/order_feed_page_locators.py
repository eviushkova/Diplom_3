from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    FIRST_ORDER_CARD = By.XPATH, ".//a[contains(@class, 'OrderHistory_link')][1]"
    OPENED_ORDER_CARD = By.XPATH, "//div[contains(@class, 'Modal_orderBox')]"
    ORDER_CARDS = By.XPATH, "//div[contains(@class, 'OrderHistory_textBox')]//p[contains(@class, 'text_type_digits')]"
    ORDER_FEED_PAGE_LOADER = By.XPATH, "//div[contains(@class, 'App_centeredComponent') and contains(text(), 'Загрузка')]"
    COMPLETED_FOR_ALL_TIME_COUNTER = By.XPATH, "//*[text()='Выполнено за все время:']/parent::div/p[2]"
    COMPLETED_FOR_TODAY_COUNTER = By.XPATH, "//*[text()='Выполнено за сегодня:']/parent::div/p[2]"
    ORDER_ID_IN_PROGRESS = By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul[2]/li"
