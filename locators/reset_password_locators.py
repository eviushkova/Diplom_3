from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    ACTIVE_PASSWORD_INPUT = By.XPATH, "//label[text()='Пароль']/parent::div/input[@type='text']"
    INACTIVE_PASSWORD_INPUT = By.XPATH,
    SHOW_PASSWORD_ICON = By.XPATH, "//div[@class='input__icon input__icon-action']"
    PASSWORD_INPUT = By.XPATH, "//label[text()='Пароль']/parent::div/input"
