from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self.wait = WebDriverWait(self.driver, 40)

    # method of get locator
    def get_locator_f(self, loc: str, by='XPATH'):
        if by == 'ID':
            locator = self.wait.until(EC.presence_of_element_located((By.ID, loc)))
            return locator
        else:
            locator = self.wait.until(EC.presence_of_element_located((By.XPATH, loc)))
            return locator

    # get locators to write to form
    first_name = property(lambda self: self.get_locator_f('//input[@name="first-name"]'))
    last_name = property(lambda self: self.get_locator_f('//input[@name="last-name"]'))
    address = property(lambda self: self.get_locator_f('//input[@name="address"]'))
    email = property(lambda self: self.get_locator_f('//input[@name="e-mail"]'))
    phone = property(lambda self: self.get_locator_f('//input[@name="phone"]'))
    city = property(lambda self: self.get_locator_f('//input[@name="city"]'))
    country = property(lambda self: self.get_locator_f('//input[@name="country"]'))
    job = property(lambda self: self.get_locator_f('//input[@name="job-position"]'))
    company = property(lambda self: self.get_locator_f('//input[@name="company"]'))
    submit_button = property(lambda self: self.get_locator_f('//button[@type="submit"]'))

    # get locators fields from form
    first_name_color = property(lambda self: self.get_locator_f('first-name', 'ID'))
    last_name_color = property(lambda self: self.get_locator_f('last-name', 'ID'))
    address_color = property(lambda self: self.get_locator_f('address', 'ID'))
    email_color = property(lambda self: self.get_locator_f('e-mail', 'ID'))
    phone_color = property(lambda self: self.get_locator_f('phone', 'ID'))
    city_color = property(lambda self: self.get_locator_f('city', 'ID'))
    country_color = property(lambda self: self.get_locator_f('country', 'ID'))
    job_color = property(lambda self: self.get_locator_f('job-position', 'ID'))
    company_color = property(lambda self: self.get_locator_f('company', 'ID'))
    zip_code_color = property(lambda self: self.get_locator_f('zip-code', 'ID'))

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

    # method of get background-color
    def get_background_color(self, loc):
        background_color = loc.value_of_css_property('background-color')
        return background_color


