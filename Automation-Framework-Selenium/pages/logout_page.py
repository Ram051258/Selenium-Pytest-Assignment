from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LogoutPage(BasePage):
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")  # Menu button
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")  # Logout button

    def logout(self):
        """Click the menu button and then the logout button."""
        self.click(self.MENU_BUTTON)
        self.wait_for_element(self.LOGOUT_BUTTON)  # Ensure menu is open
        self.click(self.LOGOUT_BUTTON)

    def verify_logout(self):
        """Check if logout was successful by verifying the login page is displayed."""
        self.wait_for_element((By.ID, "login-button"))  # Ensure login button is visible after logout
        return self.is_element_visible((By.ID, "login-button"))


    def is_element_visible(self, locator, timeout=10):
        """Check if an element is visible."""
        try:
            self.wait_for_element(locator, timeout)
            return True
        except:
            return False    
