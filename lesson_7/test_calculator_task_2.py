from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from task_2.pages.calculator import Calc

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

calc = Calc(driver)


def test_calculator():
    calc.input_sec()
    calc.calc_solution()
    assert calc.get_value() == '15', 'Answer is not 15'
    driver.quit()
