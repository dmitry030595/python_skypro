from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 40)
driver.maximize_window()

# 1. Перейдите на страницу http://uitestingplayground.com/ajax
driver.get('http://uitestingplayground.com/ajax')

# 2. Нажмите на синюю кнопку
blue_button = driver.find_element(By.ID, 'ajaxButton')
blue_button.click()

# 3. Получите текст из зеленой плашки
text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bg-success')))

# 4. Выведите его в консоль (”Data loaded with AJAX get request.”)
print(text.text)

driver.quit()
