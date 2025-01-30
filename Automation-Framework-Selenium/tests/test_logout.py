import pytest
import allure
from pages.logout_page import LogoutPage

@pytest.mark.usefixtures("setup")
@allure.feature("Logout")
class TestLogoutPage:

    @allure.story("Successful Logout")
    def test_logout(self, setup):
        """Test the logout functionality"""
        logout_page = LogoutPage(self.driver)

        with allure.step("Perform logout"):
            logout_page.logout()
