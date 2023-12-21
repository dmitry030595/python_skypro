from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from task_3.pages.total_price_page import TotalPrice
from task_3.pages.user_info_page import UserInfo
from task_3.pages.cart_page import CartPage
from task_3.pages.main_page import MainPage
from task_3.pages.registration_page import RegPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

reg = RegPage(driver)
main = MainPage(driver)
cart = CartPage(driver)
info = UserInfo(driver)
total = TotalPrice(driver)


def test_reg():
    reg.input_username()
    reg.input_password()
    reg.login_button_click()


def test_main_page():
    main.add_backpack()
    main.add_t_shirt()
    main.add_onesie()


def test_cart():
    cart.go_to_cart()
    cart.checkout_button_click()


def test_user_info():
    info.input_first_name()
    info.input_last_name()
    info.input_postal_code()
    info.continue_button_click()


def test_total_price():
    assert total.get_total_price()[7:] == '$58.29', 'total is not 58.29'
    driver.quit()
