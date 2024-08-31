# from time import sleep
from selenium import webdriver
from task_three.MainPage import MainPage
from task_three.Products import Products
from task_three.Cart import YourCart
from task_three.DataOrder import Data
from task_three.Check import Checkout


def test_shopping():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.authorization()

    product = Products(browser)
    product.add_shopping()

    cart = YourCart(browser)
    cart.get()
    cart.checkout()

    data = Data(browser)
    data.data_order()
    data.continue_button()

    check = Checkout(browser)
    total = check.summary_total()
    assert '58.29' in total

    browser.quit()
