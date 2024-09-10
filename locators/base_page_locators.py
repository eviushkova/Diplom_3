from selenium.webdriver.common.by import By


class BasePageLocators:
    LOADING_MODAL = By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
