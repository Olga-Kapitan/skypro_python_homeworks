# from time import sleep
from selenium import webdriver
# from selenium.webdriver.common.by import By
from task_2.MainPageTask2 import MainPageTask2


def test_calculator():
    browser = webdriver.Chrome()
    main_page = MainPageTask2(browser)
    main_page.clear()
    main_page.data()
    result = main_page.txt()

    assert "15" in result

    browser.quit()
