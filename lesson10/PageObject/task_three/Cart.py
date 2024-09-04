from selenium.webdriver.common.by import By


class YourCart:

    def __init__(self, browser):
        self._driver = browser

    def get(self):
        """Переход на страницу с корзиной"""
        self._driver.get("https://www.saucedemo.com/cart.html")

    def checkout(self):
        """Нажатие кнопки checkout"""
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
