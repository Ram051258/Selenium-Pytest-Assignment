import pytest
from utils.driver_factory import DriverFactory
from utils.config import Config
from pages.login_page import LoginPage  # Import the LoginPage class

@pytest.fixture(scope="class")
def setup(request):
    driver = DriverFactory.get_driver()  # Use the DriverFactory
    driver.get(Config.BASE_URL)
    driver.maximize_window()

    # Instantiate the LoginPage and perform login using credentials from Config
    login_page = LoginPage(driver)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    request.cls.driver = driver
    yield driver
    driver.quit()
