from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# 1. Перейдите на сайт: http://uitestingplayground.com/textinput
driver.get('http://uitestingplayground.com/textinput')

# 2. Укажите в поле ввода текст SkyPro
field = driver.find_element(By.ID, 'newButtonName')
field.send_keys('SkyPro')

# 3. Нажмите на синюю кнопку
blue_button = driver.find_element(By.ID, 'updatingButton')
blue_button.click()

# 4. Получите текст кнопки и выведите в консоль (“SkyPro”)
print(blue_button.text)

driver.quit()
