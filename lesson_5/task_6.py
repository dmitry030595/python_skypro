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

# 1 Откройте страницу http://the-internet.herokuapp.com/entry_ad
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)

# 2 В модальном окне нажмите на кнопку Close
button = driver.find_element(By.XPATH, "//p[contains(text(), 'Close')]")
button.click()
sleep(2)

driver.quit()
