# import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


# создать функцию по отработке заполнения
def test_filling():
    browser = webdriver.Chrome()
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    sleep(2)
    browser.find_element(
        By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    browser.find_element(
        By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")
    sleep(2)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    sleep(2)
    assert "alert-danger" in browser.find_element(
        By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert "alert-success" in browser.find_element(
        By.CSS_SELECTOR, "#first-name").get_attribute("class")
    assert "alert-success" in browser.find_element(
        By.CSS_SELECTOR, "#last-name").get_attribute("class")
    assert "alert-success" in browser.find_element(
        By.CSS_SELECTOR, "#address").get_attribute("class")
    assert "alert-success" in browser.find_element(
        By.CSS_SELECTOR, "#e-mail").get_attribute("class")
    assert "alert-success" in browser.find_element(
        By.CSS_SELECTOR, "#job-position").get_attribute("class")
    assert "alert-success" in browser.find_element(
        By.CSS_SELECTOR, "#city").get_attribute("class")
    assert "alert-success" in browser.find_element(
        By.CSS_SELECTOR, "#country").get_attribute("class")
    assert "alert-success" in browser.find_element(
        By.CSS_SELECTOR, "#phone").get_attribute("class")
    assert "alert-success" in browser.find_element(
        By.CSS_SELECTOR, "#company").get_attribute("class")
    browser.quit()

# $$(".alert-success") правильное заполнение
# $$(".alert-danger") неверное заполнение
# assert команда для проверки - использовать
# success = browser.find_elements(By.CSS_SELECTOR, ".alert-success")
# danger = browser.find_elements(By.CSS_SELECTOR, ".alert-danger")
# print("Заполнены поля: ", len(success))
# print("Поля с ошибкой: ", len(danger))

# css_red = browser.find_element(
# By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
# css_green = browser.find_element(
# By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
# print(css_red)
# print(css_green)
# color-danger: "rgba(132, 32, 41, 1)"
# color-success: "rgba(15, 81, 50, 1)"

# классы == цвету???? в чем ошибка?
# filled = browser.find_elements(By.CSS_SELECTOR, ".alert-success")
# unfilled = browser.find_elements(By.CSS_SELECTOR, ".alert-danger")
# def test_assert():
#     assert "rgba(132, 32, 41, 1)" in browser.find_element(
# By.CSS_SELECTOR, "#zip-code").value_of_css_property('color')
#     assert "rgba(15, 81, 50, 1)" in browser.find_elements(
# By.CSS_SELECTOR, ".alert-success").value_of_css_property('color')
