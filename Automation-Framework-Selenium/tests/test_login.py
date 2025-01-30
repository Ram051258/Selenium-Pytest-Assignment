import pytest
import allure
import time
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Fixture to set up and tear down the WebDriver
@pytest.fixture(scope="function", autouse=True)
def setup():
    """Initialize WebDriver before each test and quit after execution."""
    driver = DriverFactory.get_driver("chrome")
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

# Test Data
valid_users = [
    "standard_user", 
    "visual_user"  
]

invalid_users = [
    "invalid_user",
    "test_user",
    "random_user"
]

@allure.feature("Login")
@allure.story("Valid Login Scenarios")
@pytest.mark.parametrize("username", valid_users)
def test_valid_login(setup, username):
    """Test login with valid users"""
    login_page = LoginPage(setup)

    with allure.step(f"Logging in with valid user: {username}"):
        login_page.login(username, "secret_sauce")

    with allure.step("Verify login is successful"):
        assert "inventory.html" in setup.current_url, f"Login failed for {username}"


@allure.feature("Login")
@allure.story("Locked Out User")
def test_locked_out_user(setup):
    """Test login with a locked-out user (expected failure)"""
    login_page = LoginPage(setup)

    with allure.step("Logging in with locked_out_user"):
        login_page.login("locked_out_user", "secret_sauce")

    with allure.step("Verify login fails with the expected error message"):
        error_message = login_page.get_error_message()
        expected_message = "Epic sadface: Sorry, this user has been locked out."
        assert error_message == expected_message, f"Expected '{expected_message}', but got '{error_message}'"


@allure.feature("Login")
@allure.story("Error User Product Visibility")
def test_error_user(setup):
    """Test login with error_user and verify product visibility"""
    login_page = LoginPage(setup)

    with allure.step("Logging in with error_user"):
        login_page.enter_user_name("error_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

    with allure.step("Waiting for product page to load"):
        WebDriverWait(login_page.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Test.allTheThings() T-Shirt (Red)']"))
        )

    with allure.step("Verify error_user can see the specific product"):
        product_locator = (By.XPATH, "//div[text()='Test.allTheThings() T-Shirt (Red)']")
        product_element = login_page.driver.find_element(*product_locator)
        assert product_element.is_displayed(), "Product should be visible for error_user, but it was not found!"

@allure.feature("Login")
@allure.story("Invalid Login Scenarios")
@pytest.mark.parametrize("username", invalid_users)
def test_invalid_user(setup, username):
    """Test login with invalid usernames"""
    login_page = LoginPage(setup)

    with allure.step(f"Attempting login with invalid user: {username}"):
        login_page.login(username, "secret_sauce")

    with allure.step("Verify login fails with an error message"):
        error_message = login_page.get_error_message()
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        assert expected_message in error_message, f"Expected '{expected_message}', but got '{error_message}'"


@allure.feature("Login")
@allure.story("Invalid Password")
def test_invalid_password(setup):
    """Test login with a valid username but incorrect password"""
    login_page = LoginPage(setup)

    with allure.step("Logging in with incorrect password"):
        login_page.login("standard_user", "wrong_password")

    with allure.step("Verify login fails with an error message"):
        error_message = login_page.get_error_message()
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        assert expected_message in error_message, f"Expected '{expected_message}', but got '{error_message}'"


@allure.feature("Login")
@allure.story("Empty Username and Password")
@pytest.mark.parametrize("username, password", [
    ("", "secret_sauce"),  # Empty username
    ("standard_user", ""),  # Empty password
    ("", "")  # Both empty
])
def test_empty_fields(setup, username, password):
    """Test login with empty username or password"""
    login_page = LoginPage(setup)

    with allure.step(f"Attempting login with username: '{username}' and password: '{password}'"):
        login_page.login(username, password)

    with allure.step("Verify login fails with an error message"):
        error_message = login_page.get_error_message()
        assert "Username is required" in error_message or "Password is required" in error_message, \
            f"Expected 'Username is required' or 'Password is required', but got '{error_message}'"

import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Login")
@allure.story("Performance Glitch User")
def test_performance_glitch_user(setup):
    """Test login with performance_glitch_user and verify expected slight delay"""
    login_page = LoginPage(setup)

    with allure.step("Logging in with performance_glitch_user"):
        login_page.enter_user_name("performance_glitch_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

    with allure.step("Measuring delay for inventory page to load"):
        start_time = time.time()

        # Wait until the inventory page is detected (up to 10s)
        WebDriverWait(login_page.driver, 10, poll_frequency=0.5).until(
            EC.presence_of_element_located((By.ID, "inventory_container"))
        )

        end_time = time.time()
        load_time = end_time - start_time

    with allure.step(f"Verifying slight delay (Actual Load Time: {load_time:.2f}s)"):
        assert load_time <= 0.02, f"Expected ~0.02s+ delay, but inventory loaded in {load_time:.2f}s"

            
