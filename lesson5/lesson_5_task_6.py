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

# Форма авторизации
chrome.get("http://the-internet.herokuapp.com/login")
firefox.get("http://the-internet.herokuapp.com/login")

search_input_username = "#username"
search_input_password = "#password"
search_Login = ".radius"

sleep(2)

# tomsmith
# SuperSecretPassword!
chrome_username = chrome.find_element(By.CSS_SELECTOR, search_input_username)
chrome_username.send_keys("tomsmith")
firefox_username = firefox.find_element(By.CSS_SELECTOR, search_input_username)
firefox_username.send_keys("tomsmith")

sleep(2)

chrome_password = chrome.find_element(By.CSS_SELECTOR, search_input_password)
chrome_password.send_keys("SuperSecretPassword!")
firefox_password = firefox.find_element(By.CSS_SELECTOR, search_input_password)
firefox_password.send_keys("SuperSecretPassword!")

sleep(2)

chrome_login = chrome.find_element(By.CSS_SELECTOR, search_Login)
chrome_login.click()
firefox_login = firefox.find_element(By.CSS_SELECTOR, search_Login)
firefox_login.click()

sleep(2)

chrome.quit()
firefox.quit()
