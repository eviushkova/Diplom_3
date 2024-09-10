from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    EMAIL_INPUT = By.XPATH, "//label[text()='Email']/parent::div/input"
    RECOVERY_BUTTON = By.XPATH, "//button[text()='Восстановить']"
