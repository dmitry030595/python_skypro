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

# 1 Откройте страницу http://the-internet.herokuapp.com/login
driver.get("http://the-internet.herokuapp.com/login")

# 2 В поле username введите значение tomsmith
username = driver.find_element(By.ID, "username")
username.send_keys('tomsmith')
sleep(1)

# 3 В поле password введите значение SuperSecretPassword!
password = driver.find_element(By.ID, "password")
password.send_keys('SuperSecretPassword!')
sleep(1)


# 4 Нажмите кнопку Login
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()
sleep(2)

driver.quit()
