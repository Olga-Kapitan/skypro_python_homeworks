from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

browser.get("http://uitestingplayground.com/ajax")

browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

browser.implicitly_wait(20)

txt = browser.find_element(By.CSS_SELECTOR, ".bg-success").text

print(txt)

browser.quit()
