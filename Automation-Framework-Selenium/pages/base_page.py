import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def is_visible(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def get_title(self):
        return self.driver.title

    def wait_for_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def get_elements_text(self, by_locator):
        """Get the text of all elements located by the given locator."""
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        return [element.text for element in elements]   

    def click_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def find_elements(self, locator):
        """Find multiple elements using the given locator."""
        return self.driver.find_elements(*locator)    
     
