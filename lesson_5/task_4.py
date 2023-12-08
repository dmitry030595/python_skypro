from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

"""for Chrome"""
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# """for Mozilla"""
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()

# 1 Откройте страницу http://uitestingplayground.com/dynamicid
driver.get("http://uitestingplayground.com/dynamicid")

# 2 Кликните на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()
sleep(2)

driver.quit()

# 3 Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково
