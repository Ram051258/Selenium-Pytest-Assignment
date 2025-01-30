from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        if browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Browser {browser_name} is not supported.")
        return driver

def get_webdriver():
    return DriverFactory.get_driver("chrome")  # Default to Chrome or parameterize if needed
