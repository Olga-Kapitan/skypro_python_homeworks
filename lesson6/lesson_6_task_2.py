from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://uitestingplayground.com/textinput")

browser.find_element(
    By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()
txt_button = browser.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt_button)

browser.quit
