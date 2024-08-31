# from time import sleep
# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from task_1.MainPageTask1 import MainPageTask1


def test_filling():
    browser = webdriver.Chrome()
    main_page = MainPageTask1(browser)
    main_page.fill_button()
    main_page.submit()
    alert = {
        "zip-code": "alert-danger",
        "first-name": "alert-success",
        "last-name": "alert-success",
        "address": "alert-success",
        "e-mail": "alert-success",
        "job-position": "alert-success",
        "city": "alert-success",
        "country": "alert-success",
        "phone": "alert-success",
        "company": "alert-success"
    }
    for name, value in alert.items():
        assert value in browser.find_element(
            By.ID, name).get_attribute("class")

    browser.quit()
