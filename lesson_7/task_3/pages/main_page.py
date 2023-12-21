from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

    # method of get locators
    def get_locator_main(self, loc_id):
        locator = self.wait.until(EC.presence_of_element_located((By.ID, loc_id)))
        return locator

    # get locators
    add_to_cart_backpack = property(lambda self: self.get_locator_main('add-to-cart-sauce-labs-backpack'))
    add_to_cart_t_shirt = property(lambda self: self.get_locator_main('add-to-cart-sauce-labs-bolt-t-shirt'))
    add_to_cart_onesie = property(lambda self: self.get_locator_main('add-to-cart-sauce-labs-onesie'))

    # actions
    def add_backpack(self):
        self.add_to_cart_backpack.click()

    def add_t_shirt(self):
        self.add_to_cart_t_shirt.click()

    def add_onesie(self):
        self.add_to_cart_onesie.click()
