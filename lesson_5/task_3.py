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

# 1 Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# 2 Пять раз кликните на кнопку Add Element
button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
for i in range(5):
    button.click()

# 3 Соберите со страницы список кнопок Delete
lst = driver.find_elements(By.XPATH, "//button[@class='added-manually']")

# 4 Выведите на экран размер списка
print('Кол-во кнопок "Delete": ' + str(len(lst)))

sleep(5)
driver.quit()
