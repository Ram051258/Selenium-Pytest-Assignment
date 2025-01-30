from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    """ Product Detail Page class """

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "price": (By.CLASS_NAME, "inventory_details_price"),
            "add_to_cart_button": (By.CLASS_NAME, "btn_inventory"),
            "back_button": (By.CLASS_NAME, "inventory_details_back_button"),
            "product_name": (By.CLASS_NAME, "inventory_details_name"),
            "cart_item_count": (By.CLASS_NAME, "shopping_cart_badge"),
        }

    def get_element_text(self, locator_key):
        """Get the text of any element based on the locator key."""
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators[locator_key])
        )
        return element.text

    def get_price(self):
        """ Get the price of the product. """
        return self.get_element_text("price")

    def get_product_name(self):
        """Get the product's name."""
        return self.get_element_text("product_name")

    def get_number_cart_items(self):
        """Get the number of items in the cart."""
        elements = self.find_elements(self.locators["cart_item_count"])
        if elements:
            return int(elements[0].text)
        return 0

    def click_add_to_cart(self):
        """Click the add to cart button."""
        self.click_element(self.locators["add_to_cart_button"])

    def click_back(self):
        """Click the back button."""
        self.click_element(self.locators["back_button"])
