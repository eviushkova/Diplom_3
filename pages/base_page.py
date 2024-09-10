from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import data
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(BasePageLocators.LOADING_MODAL))

    def get_current_url(self):
        return self.driver.current_url

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def move_to_element_and_click(self, locator):
        element = self.find_element_with_wait(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click()
        action.perform()

    def click_on_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(BasePageLocators.LOADING_MODAL))
        self.click_on_element(locator)

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def element_exist(self, locator):
        try:
            self.find_element_with_wait(locator)
            return True
        except TimeoutException:
            return False

    def click_on_element_using_script(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    #
    def wait_until_element_becomes_invisible(self, locator):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    def wait_until_element_becomes_visible(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    def get_attribute_value(self, locator, attribute):
        attribute_value = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)).get_attribute(attribute)

        return attribute_value

    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)

        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element)
        action.perform()

    def get_list_of_elements(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(locator))

    def get_new_element_value(self, locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver, 15).until(
            lambda driver: driver.find_element(*locator).text != data.Data.BASE_ORDER_ID
        )
        new_value = self.find_element_with_wait(locator).text

        return new_value

    def get_new_element_value_in_progress(self, locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver, 15).until(
            lambda driver: driver.find_element(*locator).text != data.Data.BASE_ORDER_IN_PROGRESS_STATUS
        )
        new_value = self.find_element_with_wait(locator).text

        return new_value
