import allure
from selenium.webdriver.common.by import By


class MainPageTask1:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_button(self):
        """ Заполняет поля данными по шаблону """
        data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "job-position": "QA",
            "city": "Москва",
            "country": "Россия",
            "phone": "+7985899998787",
            "company": "SkyPro"
        }
        for name, value in data.items():
            self._driver.find_element(By.NAME, name).send_keys(value)

    def submit(self):
        """ Нажимает кнопку Submit """
        self._driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
