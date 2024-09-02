from selenium.webdriver.common.by import By


class Data:

    def __init__(self, browser):
        self._driver = browser

    def data_order(self):
        """Заполнение персональных данных(Имя, фамилия, почтовый индекс)"""
        self._driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Olga")
        self._driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Kapitanova")
        self._driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys("236000")

    def continue_button(self):
        """Нажатие кнопки Continue"""
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
