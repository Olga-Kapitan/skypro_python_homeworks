from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Модальное окно
chrome.get("http://the-internet.herokuapp.com/entry_ad")
# Firefox всплывающая реклама мешает, поэтому
# открыть браузер заранее с сайтом
firefox.get("http://the-internet.herokuapp.com/entry_ad")

sleep(2)

search_locator = ".modal-footer"
chrome_wait = WebDriverWait(chrome, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, search_locator))).click()
firefox_wait = WebDriverWait(firefox, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, search_locator))).click()

sleep(5)

chrome.quit()
firefox.quit()
