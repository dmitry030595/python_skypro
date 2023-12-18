from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 40)
driver.maximize_window()

# 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

# 2. Заполните форму значениями:
first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="first-name"]')))
first_name.send_keys('Иван')

last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="last-name"]')))
last_name.send_keys('Петров')

address = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="address"]')))
address.send_keys('Ленина, 55-3')

email = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="e-mail"]')))
email.send_keys('test@skypro.com')

phone = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="phone"]')))
phone.send_keys('+7985899998787')

city = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="city"]')))
city.send_keys('Москва')

country = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="country"]')))
country.send_keys('Россия')

job = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="job-position"]')))
job.send_keys('QA')

company = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="company"]')))
company.send_keys('SkyPro')

# 3. Нажмите кнопку Submit:
submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
submit_button.click()

# 4. Проверьте (assert), что поле Zip code подсвечено красным
zip_code = wait.until(EC.presence_of_element_located((By.ID, 'zip-code')))
zip_code_color = zip_code.value_of_css_property('background-color')


def test_zip():
    assert zip_code_color == 'rgba(248, 215, 218, 1)', 'Поле zip_code не подсвечено красным'


# 5. Проверьте (assert), что остальные поля подсвечены зеленым
first_name = wait.until(EC.presence_of_element_located((By.ID, 'first-name')))
first_name_color = first_name.value_of_css_property('background-color')

last_name = wait.until(EC.presence_of_element_located((By.ID, 'last-name')))
last_name_color = last_name.value_of_css_property('background-color')

address = wait.until(EC.presence_of_element_located((By.ID, 'address')))
address_color = address.value_of_css_property('background-color')

email = wait.until(EC.presence_of_element_located((By.ID, 'e-mail')))
email_color = email.value_of_css_property('background-color')

phone = wait.until(EC.presence_of_element_located((By.ID, 'phone')))
phone_color = phone.value_of_css_property('background-color')

city = wait.until(EC.presence_of_element_located((By.ID, 'city')))
city_color = city.value_of_css_property('background-color')

country = wait.until(EC.presence_of_element_located((By.ID, 'country')))
country_color = country.value_of_css_property('background-color')

job = wait.until(EC.presence_of_element_located((By.ID, 'job-position')))
job_color = job.value_of_css_property('background-color')

company = wait.until(EC.presence_of_element_located((By.ID, 'company')))
company_color = company.value_of_css_property('background-color')


def test_first_name():
    assert first_name_color == 'rgba(209, 231, 221, 1)', 'Поле zip_code не подсвечено зеленым'


def test_last_name():
    assert last_name_color == 'rgba(209, 231, 221, 1)', 'Поле zip_code не подсвечено зеленым'


def test_address():
    assert address_color == 'rgba(209, 231, 221, 1)', 'Поле zip_code не подсвечено зеленым'


def test_email():
    assert email_color == 'rgba(209, 231, 221, 1)', 'Поле zip_code не подсвечено зеленым'


def test_phone():
    assert phone_color == 'rgba(209, 231, 221, 1)', 'Поле zip_code не подсвечено зеленым'


def test_city():
    assert city_color == 'rgba(209, 231, 221, 1)', 'Поле zip_code не подсвечено зеленым'


def test_country():
    assert country_color == 'rgba(209, 231, 221, 1)', 'Поле zip_code не подсвечено зеленым'


def test_job():
    assert job_color == 'rgba(209, 231, 221, 1)', 'Поле zip_code не подсвечено зеленым'


def test_company():
    assert company_color == 'rgba(209, 231, 221, 1)', 'Поле zip_code не подсвечено зеленым'


driver.quit()
