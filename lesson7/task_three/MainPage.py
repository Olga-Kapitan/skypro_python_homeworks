from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# https://www.saucedemo.com/


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

# авторизация
# name = standard_user
# password = secret_sauce
    def authorization(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self._driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
