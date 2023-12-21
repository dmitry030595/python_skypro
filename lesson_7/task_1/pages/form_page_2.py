from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FormPage2:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

    # method of get locator
    def get_locator_2(self, loc_id: str):
        locator = self.wait.until(EC.presence_of_element_located((By.ID, loc_id)))
        return locator

    # get locators
    first_name = property(lambda self: self.get_locator_2('first-name'))
    last_name = property(lambda self: self.get_locator_2('last-name'))
    address = property(lambda self: self.get_locator_2('address'))
    email = property(lambda self: self.get_locator_2('e-mail'))
    phone = property(lambda self: self.get_locator_2('phone'))
    city = property(lambda self: self.get_locator_2('city'))
    country = property(lambda self: self.get_locator_2('country'))
    job = property(lambda self: self.get_locator_2('job-position'))
    company = property(lambda self: self.get_locator_2('company'))
    zip_code = property(lambda self: self.get_locator_2('zip-code'))

    # method of get background-color
    def get_background_color(self, loc):
        background_color = loc.value_of_css_property('background-color')
        return background_color

    def driver_close(self):
        self.driver.quit()
