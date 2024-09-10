from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = By.XPATH, "//a[@href='/account']"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']/parent::a"
    ORDER_FEED_BUTTON = By.XPATH, "//*[text()='Лента Заказов']/parent::a"
    FIRST_INGREDIENT = By.XPATH, "(.//a[contains(@href, '/ingredient/') and @draggable='true'])[1]"
    INGREDIENT_MODAL_HEADER = By.XPATH, './/h2[text()="Детали ингредиента"]'
    CLOSE_INGREDIENT_DETAILS_MODAL = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button"
    INGREDIENT_DETAILS_MODAL_FORM = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]"
    INGREDIENT_COUNTER = By.XPATH, ".//p[contains(@class, 'counter_counter__num')]"
    BURGER_BASKET = By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]"
    PLACE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    ORDER_STATUS = By.XPATH, "//*[contains(@class, 'Modal_modal__text')]/p[1]"
    CROSS_BUTTON_SUCCESS_ORDER_MODAL_WINDOW = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]"
    SUCCESS_ORDER_MODAL_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]"
    ORDER_NUMBER = By.XPATH, "//h2[contains(@class,'title_shadow')]"



