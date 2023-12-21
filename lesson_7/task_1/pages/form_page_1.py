from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FormPage1:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self.wait = WebDriverWait(self.driver, 40)

    # method of get locator
    def get_locator_f1(self, loc_xpath: str):
        locator = self.wait.until(EC.presence_of_element_located((By.XPATH, loc_xpath)))
        return locator

    # get locators
    first_name = property(lambda self: self.get_locator_f1('//input[@name="first-name"]'))
    last_name = property(lambda self: self.get_locator_f1('//input[@name="last-name"]'))
    address = property(lambda self: self.get_locator_f1('//input[@name="address"]'))
    email = property(lambda self: self.get_locator_f1('//input[@name="e-mail"]'))
    phone = property(lambda self: self.get_locator_f1('//input[@name="phone"]'))
    city = property(lambda self: self.get_locator_f1('//input[@name="city"]'))
    country = property(lambda self: self.get_locator_f1('//input[@name="country"]'))
    job = property(lambda self: self.get_locator_f1('//input[@name="job-position"]'))
    company = property(lambda self: self.get_locator_f1('//input[@name="company"]'))
    submit_button = property(lambda self: self.get_locator_f1('//button[@type="submit"]'))

    # method of writing text in field
    def write_some_text(self, field, text: str):
        field.send_keys(text)

    # actions
    write_first_name = property(lambda self: self.write_some_text(self.first_name, 'Иван'))
    write_last_name = property(lambda self: self.write_some_text(self.last_name, 'Петров'))
    write_address = property(lambda self: self.write_some_text(self.address, 'Ленина, 55-3'))
    write_email = property(lambda self: self.write_some_text(self.email, 'test@skypro.com'))
    write_phone = property(lambda self: self.write_some_text(self.phone, '+7985899998787'))
    write_city = property(lambda self: self.write_some_text(self.city, 'Москва'))
    write_country = property(lambda self: self.write_some_text(self.country, 'Россия'))
    write_job = property(lambda self: self.write_some_text(self.job, 'QA'))
    write_company = property(lambda self: self.write_some_text(self.company, 'SkyPro'))

    def click_submit_button(self):
        self.submit_button.click()
