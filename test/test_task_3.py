from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 40)  # P.S.: при 45 сек выпадала ошибка
driver.maximize_window()

# 1. Откройте сайт магазина: https://www.saucedemo.com/
driver.get('https://www.saucedemo.com/')

# 2. Авторизуйтесь как пользователь standard_user
username = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
username.send_keys('standard_user')

password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
password.send_keys('secret_sauce')

login_button = wait.until(EC.presence_of_element_located((By.ID, 'login-button')))
login_button.click()

# 3. Добавьте в корзину товары:
add_to_cart_backpack = wait.until(EC.presence_of_element_located((By.ID, 'add-to-cart-sauce-labs-backpack')))
add_to_cart_backpack.click()

add_to_cart_t_shirt = wait.until(EC.presence_of_element_located((By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')))
add_to_cart_t_shirt.click()

add_to_cart_onesie = wait.until(EC.presence_of_element_located((By.ID, 'add-to-cart-sauce-labs-onesie')))
add_to_cart_onesie.click()

# 4. Перейдите в корзину
cart = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="shopping_cart_link"]')))
cart.click()

# 5. Нажмите Checkout
checkout_button = wait.until(EC.presence_of_element_located((By.ID, 'checkout')))
checkout_button.click()

# 6. Заполните форму своими данными:
first_name = wait.until(EC.presence_of_element_located((By.ID, 'first-name')))
first_name.send_keys("Dmitry")

last_name = wait.until(EC.presence_of_element_located((By.ID, 'last-name')))
last_name.send_keys("Malnev")

postal_code = wait.until(EC.presence_of_element_located((By.ID, 'postal-code')))
postal_code.send_keys("105487")


# 7. Нажмите кнопку Continue
continue_button = wait.until(EC.presence_of_element_located((By.ID, 'continue')))
continue_button.click()


# 8. Прочитайте со страницы итоговую стоимость (Total)
total = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label')))
total = total.text[7:]


# 9. Закройте браузер
driver.quit()


# Проверьте, что итоговая сумма равна $58.29
def test_total_price():
    assert total == '$58.29', 'total is not 58.29'
