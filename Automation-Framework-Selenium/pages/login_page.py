from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name_placeholder = (By.ID, "user-name")
        self.password_placeholder = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.err_msg_container = (By.CSS_SELECTOR, "div h3")
        self.error_user_product =(By.XPATH, "//div[text()='Test.allTheThings() T-Shirt (Red)']")

    def enter_user_name(self, user_name):
        self.driver.find_element(*self.user_name_placeholder).send_keys(user_name)

    def enter_password(self, password):
        self.driver.find_element(*self.password_placeholder).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.err_msg_container).text

    def valid_login(self):
        self.enter_user_name("standard_user")
        self.enter_password("secret_sauce")
        self.click_login_button()
        return ProductsPage(self.driver)

    def login(self, user_name, password):
        """Generic login method to allow any username and password"""
        self.enter_user_name(user_name)
        self.enter_password(password)
        self.click_login_button()  
        time.sleep(3)  
        
