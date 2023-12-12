from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 40)
driver.maximize_window()

# 1. Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

# 2. Дождитесь загрузки всех картинок
wait.until(EC.presence_of_element_located((By.ID, 'landscape')))

# 3. Получите значение атрибута `src` у 3-й картинки
value = driver.find_element(By.ID, 'award')

# 4. Выведите значение в консоль
print(value.get_attribute('src'))
