from selenium.webdriver.common.by import By


class AccountPageLocators:
    ORDER_HISTORY_BUTTON = By.XPATH, "//a[@href='/account/order-history']"
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']"
    ACCOUNT_BUTTON = By.XPATH, "//a[@href='/account']"
    USER_ORDERS = By.XPATH, "//div[contains(@class, 'OrderHistory_textBox')]//p[contains(@class, 'text_type_digits')]"
    ORDER_HISTORY_LOADER = By.XPATH, "//div[contains(@class, 'App_centeredComponent') and contains(text(), 'Загрузка')]"
    LOADING_MODAL = By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
