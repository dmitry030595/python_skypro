from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

    # method of get locators
    def get_locator_cart(self, loc_id):
        locator = self.wait.until(EC.presence_of_element_located((By.ID, loc_id)))
        return locator

    # get locators
    checkout_button = property(lambda self: self.get_locator_cart('checkout'))

    # actions
    def go_to_cart(self):
        self.driver.get('https://www.saucedemo.com/cart.html')

    def checkout_button_click(self):
        self.checkout_button.click()
