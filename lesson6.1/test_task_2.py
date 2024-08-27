# from time import sleep
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator(browser):
    # browser = webdriver.Chrome()
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    browser.find_element(By.CSS_SELECTOR, "#delay").clear()
    browser.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)
    browser.find_element(By.XPATH, '//span[text()="7"]').click()
    browser.find_element(By.XPATH, '//span[text()="+"]').click()
    browser.find_element(By.XPATH, '//span[text()="8"]').click()
    browser.find_element(By.XPATH, '//span[text()="="]').click()
    # browser.implicitly_wait(46)
    wait = WebDriverWait(browser, 46)
    wait.until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR, 'div.screen'), "15"))
    result = browser.find_element(By.CSS_SELECTOR, 'div.screen').text
    assert "15" in result
    print(result)
    # browser.quit()
