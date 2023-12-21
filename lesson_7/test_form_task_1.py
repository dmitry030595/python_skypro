from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from task_1.pages.form_page_1 import FormPage1
from task_1.pages.form_page_2 import FormPage2

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

form_1 = FormPage1(driver)
form_2 = FormPage2(driver)


def test_write_to_form():
    form_1.write_first_name
    form_1.write_last_name
    form_1.write_address
    form_1.write_email
    form_1.write_phone
    form_1.write_city
    form_1.write_country
    form_1.write_job
    form_1.write_company
    form_1.click_submit_button()


def test_zip_code_color():
    assert form_2.get_background_color(form_2.zip_code) == 'rgba(248, 215, 218, 1)', ('Поле zip_code не подсвечено '
                                                                                      'красным')


def test_first_name_color():
    assert form_2.get_background_color(form_2.first_name) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                        'зеленым')


def test_last_name_color():
    assert form_2.get_background_color(form_2.last_name) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                       'зеленым')


def test_address_color():
    assert form_2.get_background_color(form_2.address) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                     'зеленым')


def test_email_color():
    assert form_2.get_background_color(form_2.email) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                   'зеленым')


def test_phone_color():
    assert form_2.get_background_color(form_2.phone) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                   'зеленым')


def test_city_color():
    assert form_2.get_background_color(form_2.city) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                  'зеленым')


def test_country_color():
    assert form_2.get_background_color(form_2.country) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                     'зеленым')


def test_job_color():
    assert form_2.get_background_color(form_2.job) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                 'зеленым')


def test_company_color():
    assert form_2.get_background_color(form_2.company) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                     'зеленым')
    form_2.driver_close()
