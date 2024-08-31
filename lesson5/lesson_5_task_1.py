from time import sleep

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

# chrome = webdriver.Chrome(
# service=ChromeService(ChromeDriverManager().install()))
# firefox = webdriver.Firefox(
# service=FirefoxService(GeckoDriverManager().install()))

# Клик по кнопке
chrome.get('http://the-internet.herokuapp.com/add_remove_elements/')
firefox.get('http://the-internet.herokuapp.com/add_remove_elements/')

search_locator = '[onclick="addElement()"]'
chrome_button = chrome.find_element(By.CSS_SELECTOR, search_locator)
firefox_button = firefox.find_element(By.CSS_SELECTOR, search_locator)

for click in range(5):
    chrome_button.click()
    firefox_button.click()
    sleep(2)

search_locator2 = ".added-manually"
chrome_search_delete = chrome.find_elements(By.CSS_SELECTOR, search_locator2)
firefox_search_delete = firefox.find_elements(By.CSS_SELECTOR, search_locator2)

print("Cписок кнопок Delete Chrome: ", + len(chrome_search_delete))
print("Cписок кнопок Delete Firefox: ", + len(firefox_search_delete))

chrome.quit()
firefox.quit()
