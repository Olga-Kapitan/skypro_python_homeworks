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

# Поле ввода
chrome.get("http://the-internet.herokuapp.com/inputs")
firefox.get("http://the-internet.herokuapp.com/inputs")

sleep(2)

search_locator = 'input'

chrome_search_input = chrome.find_element(By.CSS_SELECTOR, search_locator)
chrome_search_input.send_keys(1000)

firefox_search_input = firefox.find_element(By.CSS_SELECTOR, search_locator)
firefox_search_input.send_keys(1000)

sleep(2)

chrome_search_input.clear()
firefox_search_input.clear()

sleep(2)

chrome_search_input = chrome.find_element(By.CSS_SELECTOR, search_locator)
chrome_search_input.send_keys(999)

firefox_search_input = firefox.find_element(By.CSS_SELECTOR, search_locator)
firefox_search_input.send_keys(999)

sleep(2)

chrome.quit()
firefox.quit()
