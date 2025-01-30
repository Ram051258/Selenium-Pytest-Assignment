from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH,'//*[@id="add-to-cart"]')
    CART_ICON = (By.XPATH,'//*[@id="shopping_cart_container"]/a/span')
    BACK_BUTTON = (By.XPATH,'//*[@id="back-to-products"]')
    BACKPACK_ITEM = (By.XPATH,'//*[@id="item_4_title_link"]/div')
    JACKET_ITEM = (By.XPATH,'//*[@id="item_5_title_link"]/div')



    def add_product_to_cart(self):
        self.click(self.BACKPACK_ITEM)
        self.click(self.ADD_TO_CART_BUTTON)
        self.click(self.BACK_BUTTON)
        self.click(self.JACKET_ITEM)
        self.click(self.ADD_TO_CART_BUTTON)
        self.click(self.BACK_BUTTON)
        self.click(self.CART_ICON)     

    def go_to_cart(self):
        self.click(self.CART_ICON)        