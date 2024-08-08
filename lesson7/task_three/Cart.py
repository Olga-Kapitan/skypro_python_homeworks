from selenium.webdriver.common.by import By


class YourCart:

    def __init__(self, browser):
        self._driver = browser

    # перейти в корзину
    def get(self):
        self._driver.get("https://www.saucedemo.com/cart.html")

    # кнопка checkout
    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
