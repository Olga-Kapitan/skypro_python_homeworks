# import pytest
from time import sleep
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


# создать функцию по отработке заполнения
def test_filling(browser):
    # browser = webdriver.Chrome()
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
