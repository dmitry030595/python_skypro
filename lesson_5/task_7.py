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

# 1 Откройте страницу http://the-internet.herokuapp.com/inputs
driver.get("http://the-internet.herokuapp.com/inputs")

# 2 Введите в поле текст 1000
field = driver.find_element(By.XPATH, "//input[@type='number']")
field.send_keys(1000)
sleep(2)

# 3 Очистите это поле (метод clear)
field.clear()


# 4 Введите в это же поле текст 999
field.send_keys(999)
sleep(2)

driver.quit()
