from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class ProductListPage(BasePage):
    """ Page Object Model for the Product List Page (PLP). """

    ADD_TO_CART_BUTTON_XPATH = "//button[starts-with(@id, 'add-to-cart-')]"
    REMOVE_BUTTON_TEXT_XPATH ="//button[@id='remove-sauce-labs-bolt-t-shirt']"
    URL_XPATH = ".//div[2]/a"

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "add_to_cart_buttons": (By.CLASS_NAME, "btn_primary"),
            "hamburger_menu": (By.CSS_SELECTOR, "#menu_button_container button"),
            "cart_item_count": (By.CLASS_NAME, "shopping_cart_badge"),
            "cart": (By.CLASS_NAME, "shopping_cart_link"),
            "inventory_item_name": (By.CLASS_NAME, "inventory_item_name"),
            "inventory_item_price": (By.CLASS_NAME, "inventory_item_price"),
            "inventory_item": (By.CLASS_NAME, "inventory_item"),
            "inventory_list": (By.CLASS_NAME, "inventory_list"),
            "sort_menu": (By.CLASS_NAME, "product_sort_container"),
            "subheader": (By.CLASS_NAME, "product_label"),
        }

    def click_cart(self):
        self.click_element(self.locators["cart"])

    def click_hamburger_menu(self):
        self.click_element(self.locators["hamburger_menu"])

    def click_sort_menu(self):
        self.click_element(self.locators["sort_menu"])

    def get_product_names(self):
        return self.get_elements_text(self.locators["inventory_item_name"])

    def get_product_prices(self):
        return [float(price.replace("$", "")) for price in self.get_elements_text(self.locators["inventory_item_price"])]

    def get_cart_item_count(self):
        """Get the number of items in the cart."""
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.locators["cart_item_count"])
            )
            return int(elements[0].text) if elements else 0
        except Exception as e:
            print(f"Error getting cart item count: {e}")
            return 0

    def add_all_to_cart(self):
        for product in self.find_elements(self.locators["inventory_item"]):
            product.find_element(By.XPATH, self.ADD_TO_CART_BUTTON_XPATH).click()

    def click_sort_menu(self):
        """Wait for the sort menu to be clickable and click it."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locators["sort_menu"])).click()

    def sort_products(self, sort_value):
        """Sort products based on the provided sort value ('az', 'za', 'lohi', 'hilo')."""
        self.click_sort_menu()  # Ensure dropdown is clicked

        # Use Select class to choose the sorting option
        select = Select(self.driver.find_element(*self.locators["sort_menu"]))
        select.select_by_value(sort_value)  # Select option by its value 

    def get_all_product_elements(self):
        """ Get all product elements on the PLP. """
        return self.find_elements(self.locators["inventory_item"])       

