from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageTask2:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def clear(self):
        """
            Очищает поле ввода времени ожидания.

            Вводит значение по шаблону 45 секунд.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)

    def data(self):
        """ Нажимает кнопки на калькуляторе по шаблону 7+8=

            Ожидает появления ответа калькулятора (Ответ:15)
        """
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()
        wait = WebDriverWait(self._driver, 46)
        wait.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, 'div.screen'), "15"))

    def txt(self) -> int:
        """Возвращает ответ калькулятора"""
        return self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
