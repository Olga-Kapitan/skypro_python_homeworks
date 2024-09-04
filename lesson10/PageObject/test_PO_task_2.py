import allure
from selenium import webdriver
from task_2.MainPageTask2 import MainPageTask2


@allure.epic("Калькулятор")
@allure.title("Сложение по чисел")
@allure.severity("blocker")
def test_calculator():
    browser = webdriver.Chrome()
    main_page = MainPageTask2(browser)
    with allure.step("Очистить поле ожидания и ввести занчение 45 секунд"):
        main_page.clear()
    with allure.step("Выполнить сложение по шаблону 7+8="):
        main_page.data()
    with allure.step("Получить ответ калькулятора"):
        result = main_page.txt()
    with allure.step("Проверить, что значение соответствует ответу калькулятора"):
        assert "15" in result
    with allure.step("Закрыть браузер"):
        browser.quit()
