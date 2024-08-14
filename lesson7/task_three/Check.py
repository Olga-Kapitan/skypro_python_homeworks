from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, browser):
        self._driver = browser

    # Прочитайте со страницы итоговую стоимость Total
    # Проверьте, что итоговая сумма равна $58.29
    def summary_total(self):
        return self._driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text
