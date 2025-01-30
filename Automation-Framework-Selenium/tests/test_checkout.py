import pytest
import allure
from pages.product_page import ProductPage
from pages.cart_and_checkout_page import CartandCheckoutPage

@pytest.mark.usefixtures("setup")
class TestCheckoutPage:

    @allure.feature('Product Purchase')
    @allure.story('Adding product to cart')
    @allure.step('Add product to the cart')
    def test_add_product_to_cart(self):
        product_page = ProductPage(self.driver)
        product_page.add_product_to_cart()

    @allure.feature('Cart Actions')
    @allure.story('Navigating to the cart')
    @allure.step('Go to the cart page')
    def test_go_to_cart(self):
        product_page = ProductPage(self.driver)
        product_page.go_to_cart()
        assert "cart.html" in self.driver.current_url, "Failed to add product to cart!"

    @allure.feature('Checkout Process')
    @allure.story('Checkout flow')
    @allure.step('Initiating checkout')
    def test_checkout(self):
        cart_page = CartandCheckoutPage(self.driver)
        cart_page.checkout()

    @allure.feature('Checkout Process')
    @allure.story('Entering customer info')
    @allure.step('Enter customer info and finish checkout')
    def test_enter_customer_info(self):
        checkout_page = CartandCheckoutPage(self.driver)
        checkout_page.enter_customer_info("Ram", "Sri", "12345")
        checkout_page.finish_checkout()
        assert "checkout-complete.html" in self.driver.current_url, "Checkout failed!"
        checkout_page.back_home()
