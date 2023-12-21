from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TotalPrice:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

    # method of get locators
    def get_locator_price(self, loc):
        locator = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, loc)))
        return locator

    # get locators
    total = property(lambda self: self.get_locator_price('summary_total_label'))

    # methods
    def get_total_price(self):
        total_price = self.total.text
        return total_price
