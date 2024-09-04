import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from task_1.MainPageTask1 import MainPageTask1


@allure.epic("Заполнение формы")
@allure.title("Заполнение формы и нажатие на кнопку отправить")
@allure.severity("blocker")
def test_filling():
    browser = webdriver.Chrome()
    main_page = MainPageTask1(browser)
    with allure.step("Заполнить поля по шаблону"):
        main_page.fill_button()
    with allure.step("Нажать кнопку Submit"):
        main_page.submit()
    alert = {
        "zip-code": "alert-danger",
        "first-name": "alert-success",
        "last-name": "alert-success",
        "address": "alert-success",
        "e-mail": "alert-success",
        "job-position": "alert-success",
        "city": "alert-success",
        "country": "alert-success",
        "phone": "alert-success",
        "company":
        "alert-success"
    }
    with allure.step("проверить соответствие заполненных полей к алерту цвета"):
        for name, value in alert.items():
            assert value in browser.find_element(
                By.ID, name).get_attribute("class")
    with allure.step("Закрыть браузер"):
        browser.quit()
