import allure
from selenium import webdriver
from task_three.MainPage import MainPage
from task_three.Products import Products
from task_three.Cart import YourCart
from task_three.DataOrder import Data
from task_three.Check import Checkout


@allure.epic("Магазин")
@allure.title("Покупка товара")
@allure.severity("blocker")
def test_shopping():
    browser = webdriver.Chrome()

    with allure.step("Авторизация на странице магазина"):
        main_page = MainPage(browser)
        main_page.authorization()
    with allure.step("Добавить три товара в корзину"):
        product = Products(browser)
        product.add_shopping()
    with allure.step("Перейти на страницу с корзиной"):
        cart = YourCart(browser)
        cart.get()
    with allure.step("Нажать кнопку checkout"):
        cart.checkout()
    with allure.step("Заполнить персональные данные для заказа"):
        data = Data(browser)
        data.data_order()
    with allure.step("Нажать кнопку continue"):
        data.continue_button()
    with allure.step("Получить итогую сумму заказа"):
        check = Checkout(browser)
        total = check.summary_total()
    with allure.step("Сравнить значение с итоговой суммой"):
        assert '58.29' in total
    with allure.step("Закрыть браузер"):
        browser.quit()
