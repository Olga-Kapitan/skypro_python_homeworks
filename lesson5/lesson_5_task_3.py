from time import sleep

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
firefox.set_window_position(600, 10)

# chrome = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()))
# firefox = webdriver.Firefox(
#     service=FirefoxService(GeckoDriverManager().install()))

# Клик по кнопке с CSS-классом
chrome.get("http://uitestingplayground.com/classattr")
firefox.get("http://uitestingplayground.com/classattr")

search_locator = ".btn-primary"
chrome_blue_button = chrome.find_element(
    By.CSS_SELECTOR, search_locator).click()
firefox_blue_button = firefox.find_element(
    By.CSS_SELECTOR, search_locator).click()

sleep(2)

chrome.switch_to.alert.accept()
firefox.switch_to.alert.accept()

for blue in range(3):
    count = 0
    chrome_blue_button = chrome.find_element(
        By.CSS_SELECTOR, search_locator).click()
    firefox_blue_button = firefox.find_element(
        By.CSS_SELECTOR, search_locator).click()
    chrome.switch_to.alert.accept()
    sleep(2)
    firefox.switch_to.alert.accept()
    sleep(2)
    count = blue + 1
    print(count)

sleep(2)

chrome.quit()
firefox.quit()
