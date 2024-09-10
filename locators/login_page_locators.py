from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOADING_MODAL = By.XPATH, "//*[contains(@class, 'Modal_modal__loading')]/following::div[contains(@class, 'Modal_modal_overlay')]"
    FORGOT_PASSWORD_LINK = By.XPATH, "//a[@href='/forgot-password']"
    PASSWORD_INPUT = By.XPATH, "//label[text()='Пароль']/parent::div/input"
    REGISTER_LINK = By.XPATH, "//a[@href='/register']"
    LOGIN_BUTTON = By.XPATH, "//*[text()='Войти']"
