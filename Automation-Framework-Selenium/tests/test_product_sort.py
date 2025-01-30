import time
import pytest
import allure
from pages.login_page import LoginPage
import lib.LoginCreds as LoginCreds
from selenium.webdriver.common.by import By
from pages.product_list_page import ProductListPage
from utils.driver_factory import DriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to set up and tear down the WebDriver
@pytest.fixture(scope="function")
def setup():
    """Initialize WebDriver before each test and quit after execution."""
    driver = DriverFactory.get_driver("chrome")
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_fixture(setup):
    """Logs in before each test that requires authentication."""
    login_page = LoginPage(setup)
    
    with allure.step("Logging in with valid user: standard_user"):
        login_page.login("standard_user", "secret_sauce")
    
    with allure.step("Verify login is successful"):
        assert "inventory.html" in setup.current_url, "Login failed, inventory page not found"

    return setup  # Return the driver after login

@allure.feature("Product List")
@allure.story("Get Product Names")
def test_get_products(login_fixture):
    """Test getting all product names from the PLP (Product List Page)."""
    product_list_page = ProductListPage(login_fixture)

    # Fetch product names
    with allure.step("Get product names from the product list page"):
        product_names = product_list_page.get_product_names()
        allure.attach(str(product_names), name="Product Names", attachment_type=allure.attachment_type.TEXT)

    # Verify there are products listed
    with allure.step("Verify there are products listed"):
        assert len(product_names) > 0, "No products found"

    # Verify expected products exist
    expected_products = {"Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"}
    with allure.step("Verify expected products are present"):
        assert expected_products.issubset(set(product_names)), f"Some expected products are missing! Found: {product_names}"

@allure.feature("Product List")
@allure.story("Sort Products A to Z")
def test_sort_a_to_z(login_fixture):
    """Test sorting the PLP's products in alphabetical order."""
    product_page = ProductListPage(login_fixture)

    with allure.step("Sorting products from A to Z"):
        product_page.sort_products("az")  # Use 'az' for A-Z sorting

    with allure.step("Fetching sorted product names"):
        product_names = product_page.get_product_names()
        allure.attach(str(product_names), name="Sorted Product Names", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Verifying products are sorted in ascending order"):
        for i in range(len(product_names) - 1):
            assert product_names[i] <= product_names[i + 1], \
                f"Products '{product_names[i]}' and '{product_names[i+1]}' are not in correct order."

    allure.attach("Sorting A-Z test passed successfully.", name="Test Result", attachment_type=allure.attachment_type.TEXT)


@allure.feature("Product List")
@allure.story("Sort Products Z to A")
def test_sort_z_to_a(login_fixture):
    """Test sorting the PLP's products in reverse alphabetical order (Z to A)."""
    product_page = ProductListPage(login_fixture)

    with allure.step("Sorting products from Z to A"):
        product_page.sort_products("za")  # Use 'za' for Z-A sorting

    with allure.step("Fetching sorted product names"):
        product_names = product_page.get_product_names()
        allure.attach(str(product_names), name="Sorted Product Names", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Verifying products are sorted in descending order"):
        for i in range(len(product_names) - 1):
            assert product_names[i] >= product_names[i + 1], \
                f"Products '{product_names[i]}' and '{product_names[i+1]}' are not in correct order."

    allure.attach("Sorting Z-A test passed successfully.", name="Test Result", attachment_type=allure.attachment_type.TEXT)

@allure.feature("Product List")
@allure.story("Sort Products Low to High")
def test_sort_low_to_high(login_fixture):
    """Test sorting the PLP's products by price from low to high."""
    product_page = ProductListPage(login_fixture)

    with allure.step("Sorting products from Low to High price"):
        product_page.sort_products("lohi")  # Use 'lohi' for Low to High sorting

    with allure.step("Fetching sorted product prices"):
        product_prices = product_page.get_product_prices()
        allure.attach(str(product_prices), name="Sorted Product Prices", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Verifying products are sorted by price in ascending order"):
        for i in range(len(product_prices) - 1):
            assert product_prices[i] <= product_prices[i + 1], \
                f"Prices '{product_prices[i]}' and '{product_prices[i+1]}' are not in correct order."

    allure.attach("Sorting Low to High test passed successfully.", name="Test Result", attachment_type=allure.attachment_type.TEXT)

@allure.feature("Product List")
@allure.story("Sort Products High to Low")
def test_sort_high_to_low(login_fixture):
    """Test sorting the PLP's products by price from high to low."""
    product_page = ProductListPage(login_fixture)

    with allure.step("Sorting products from High to Low price"):
        product_page.sort_products("hilo")  # Use 'hilo' for High to Low sorting

    with allure.step("Fetching sorted product prices"):
        product_prices = product_page.get_product_prices()
        allure.attach(str(product_prices), name="Sorted Product Prices", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Verifying products are sorted by price in descending order"):
        for i in range(len(product_prices) - 1):
            assert product_prices[i] >= product_prices[i + 1], \
                f"Prices '{product_prices[i]}' and '{product_prices[i+1]}' are not in correct order."

    allure.attach("Sorting High to Low test passed successfully.", name="Test Result", attachment_type=allure.attachment_type.TEXT)


