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

# Клик по кнопке без ID
chrome.get('http://uitestingplayground.com/dynamicid')
firefox.get('http://uitestingplayground.com/dynamicid')

search_locator = ".btn"
chrome_search_button = chrome.find_element(
    By.CSS_SELECTOR, search_locator).click()
firefox_search_button = firefox.find_element(
    By.CSS_SELECTOR, search_locator).click()

for click in range(3):
    count = 0
    chrome_search_button = chrome.find_element(
        By.CSS_SELECTOR, search_locator).click()
    firefox_search_button = firefox.find_element(
        By.CSS_SELECTOR, search_locator).click()
    count = click + 1
    print(count)
    sleep(2)

chrome.quit()
firefox.quit()
