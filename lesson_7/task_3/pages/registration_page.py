from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class RegPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')
        self.wait = WebDriverWait(self.driver, 40)

    # method of get locators
    def get_locator_reg(self, loc_id):
        locator = self.wait.until(EC.presence_of_element_located((By.ID, loc_id)))
        return locator

    # get locators
    username = property(lambda self: self.get_locator_reg('user-name'))
    password = property(lambda self: self.get_locator_reg('password'))
    login_button = property(lambda self: self.get_locator_reg('login-button'))

    # actions
    def input_username(self):
        self.username.send_keys('standard_user')

    def input_password(self):
        self.password.send_keys('secret_sauce')

    def login_button_click(self):
        self.login_button.click()
