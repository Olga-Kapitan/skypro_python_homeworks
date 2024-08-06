# from time import sleep
from selenium import webdriver
from task_3.MainPageTask3 import MainPageTask3
from task_3.Products import Products
from task_3.Cart import YourCart
from task_3.DataOrder import Data
from task_3.CheckoutOverview import CheckoutOverview


def shopping():
    browser = webdriver.Chrome()

    main_page = MainPageTask3(browser)
    main_page.authorization()

    product = Products(browser)
    product.add_shopping()

    cart = YourCart(browser)
    cart.get()
    cart.checkout()

    data = Data(browser)
    data.data_order()
    data.continue_button()

    check = CheckoutOverview(browser)
    total = check.summary_total()
    assert '58.29' in total

    browser.quit()
