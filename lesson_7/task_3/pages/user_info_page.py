from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserInfo:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

    # method of get locators
    def get_locator_info(self, loc_id):
        locator = self.wait.until(EC.presence_of_element_located((By.ID, loc_id)))
        return locator

    # get locators
    first_name = property(lambda self: self.get_locator_info('first-name'))
    last_name = property(lambda self: self.get_locator_info('last-name'))
    postal_code = property(lambda self: self.get_locator_info('postal-code'))
    continue_button = property(lambda self: self.get_locator_info('continue'))

    # actions
    def input_first_name(self):
        self.first_name.send_keys('Dmitry')

    def input_last_name(self):
        self.last_name.send_keys('Malnev')

    def input_postal_code(self):
        self.postal_code.send_keys('105487')

    def continue_button_click(self):
        self.continue_button.click()
