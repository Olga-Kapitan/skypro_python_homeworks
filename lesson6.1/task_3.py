# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.get(" https://www.saucedemo.com/.")

# авторизация
# name = standard_user
# password = secret_sauce
browser.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
browser.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
browser.find_element(By.CSS_SELECTOR, "#login-button").click()

# Добавить в корзину товары
browser.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
browser.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
browser.find_element(
    By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

# перейти в корзину
browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

# кнопка checkout
browser.find_element(By.CSS_SELECTOR, "#checkout").click()

# заполнить форму : Имя, фамилия, почт индекс
browser.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Olga")
browser.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Kapitanova")
browser.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("236000")

# кнопка Continue
browser.find_element(By.CSS_SELECTOR, "#continue").click()

# Прочитайте со страницы итоговую стоимость Total
# Проверьте, что итоговая сумма равна $58.29
txt = browser.find_element(By.CSS_SELECTOR, ".summary_total_label").text
print(txt)
assert '58.29' in browser.find_element(
    By.CSS_SELECTOR, ".summary_total_label").text

browser.quit()
