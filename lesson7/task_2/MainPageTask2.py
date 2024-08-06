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
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)

    def data(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()
        wait = WebDriverWait(self._driver, 46)
        wait.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, 'div.screen'), "15"))

    def txt(self):
        self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
