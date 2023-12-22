from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from task_1.pages.form_page import FormPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

form = FormPage(driver)


def test_check_color():
    form.write_first_name
    form.write_last_name
    form.write_address
    form.write_email
    form.write_phone
    form.write_city
    form.write_country
    form.write_job
    form.write_company
    form.click_submit_button()

    assert form.get_background_color(form.zip_code_color) == 'rgba(248, 215, 218, 1)', ('Поле zip_code не подсвечено '
                                                                                        'красным')
    assert form.get_background_color(form.first_name_color) == 'rgba(209, 231, 221, 1)', ('Поле first_name не '
                                                                                          'подсвечено зеленым')
    assert form.get_background_color(form.last_name_color) == 'rgba(209, 231, 221, 1)', ('Поле first_name не '
                                                                                         'подсвечено зеленым')
    assert form.get_background_color(form.address_color) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено'
                                                                                       'зеленым')
    assert form.get_background_color(form.email_color) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                     'зеленым')
    assert form.get_background_color(form.phone_color) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                     'зеленым')
    assert form.get_background_color(form.city_color) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                    'зеленым')
    assert form.get_background_color(form.country_color) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено'
                                                                                       'зеленым')
    assert form.get_background_color(form.job_color) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено '
                                                                                   'зеленым')
    assert form.get_background_color(form.company_color) == 'rgba(209, 231, 221, 1)', ('Поле first_name не подсвечено'
                                                                                       'зеленым')
    driver.quit()
