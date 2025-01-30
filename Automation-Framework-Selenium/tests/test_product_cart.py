import pytest
import allure
from pages.product_page import ProductPage
from pages.product_list_page import ProductListPage

@pytest.mark.usefixtures("setup")
@allure.feature("Product Page")  # Feature-level annotation
class TestProductPage:
    
    @allure.story("Add Product to Cart")  # Story annotation
    @allure.step("Adding product to the cart")  # Step annotation
    def test_add_product_to_cart(self):
        product_page = ProductPage(self.driver)
        product_page.add_product_to_cart()

    @allure.story("Go to Cart")  # Story annotation
    @allure.step("Navigating to cart and verifying the URL")  # Step annotation
    def test_go_to_cart(self):
        product_page = ProductPage(self.driver)       
        product_page.go_to_cart()
        assert "cart.html" in self.driver.current_url, "Failed to add product to cart!"
