from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 50)  # P.S.: при 45 сек выпадала ошибка
driver.maximize_window()

# 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

# 2. В поле ввода по локатору #delay введите значение 45:
sec = wait.until(EC.presence_of_element_located((By.ID, 'delay')))
sec.clear()
sec.send_keys('45')

# 3. Нажмите на кнопки '7', '+', '8', '=':
seven = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "7")]')))
seven.click()

plus = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "+")]')))
plus.click()

eight = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "8")]')))
eight.click()

equals = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "=")]')))
equals.click()

# 4. Проверьте (assert), что в окне отобразится результат 15 через 45 секунд
value = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="screen" and contains(text(), "15")]')))
value = value.text


def test_calculator():
    assert value == '15'


driver.quit()
