from selenium import webdriver
from MainPage import MainPage


def test_full():
    
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.fill_fields()
    main_page.submit()

    assert main_page.is_zip()
    assert main_page.is_first_name()
    assert main_page.is_last_name()
    assert main_page.is_address()
    assert main_page.is_city()
    assert main_page.is_country()
    assert main_page.is_email()
    assert main_page.is_phone()
    assert main_page.is_job()
    assert main_page.is_company()

    driver.close()
