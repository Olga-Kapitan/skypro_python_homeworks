from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, browser):
        self._driver = browser

    def summary_total(self):
        """Получение итоговой суммы заказа"""
        return self._driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
