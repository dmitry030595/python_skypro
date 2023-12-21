from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Calc:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self.wait = WebDriverWait(self.driver, 50)  # P.S.: при 45 сек выпадала ошибка

    # method of get locator
    def get_locator_calc(self, loc: str, by='XPATH'):
        if by == 'ID':
            locator = self.wait.until(EC.presence_of_element_located((By.ID, loc)))
            return locator
        else:
            locator = self.wait.until(EC.presence_of_element_located((By.XPATH, loc)))
            return locator

    # get locators
    sec = property(lambda self: self.get_locator_calc('delay', 'ID'))
    seven = property(lambda self: self.get_locator_calc('//span[contains(text(), "7")]'))
    plus = property(lambda self: self.get_locator_calc('//span[contains(text(), "+")]'))
    eight = property(lambda self: self.get_locator_calc('//span[contains(text(), "8")]'))
    equals = property(lambda self: self.get_locator_calc('//span[contains(text(), "=")]'))
    value = property(lambda self: self.get_locator_calc('//div[@class="screen" and contains(text(), "15")]'))

    # actions
    def input_sec(self):
        self.sec.clear()
        self.sec.send_keys('45')

    def calc_solution(self):
        """Ввод примера в калькулятор"""
        for i in [self.seven, self.plus, self.eight, self.equals]:
            i.click()

    def get_value(self):
        value = self.value.text
        return value
