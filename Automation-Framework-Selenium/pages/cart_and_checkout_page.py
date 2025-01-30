from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartandCheckoutPage(BasePage):
    FIRST_NAME = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME = (By.XPATH, '//*[@id="last-name"]')
    POSTAL_CODE = (By.XPATH, '//*[@id="postal-code"]')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="cancel"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="continue"]')
    FINISH_BUTTON = (By.XPATH, '//*[@id="finish"]')
    BACKHOME_BUTTON = (By.XPATH, '//*[@id="back-to-products"]')
    CART_ICON = (By.XPATH,'//*[@id="shopping_cart_container"]/a/span')
    CHECKOUT_BUTTON =(By.XPATH, '//*[@id="checkout"]')

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)


    def enter_customer_info(self,first_name,last_name,postal_code):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.POSTAL_CODE, postal_code)

    def finish_checkout(self):    
        self.click(self.CONTINUE_BUTTON)
        self.click(self.FINISH_BUTTON)
        
    def back_home(self):    
        self.click(self.BACKHOME_BUTTON)