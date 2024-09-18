from selenium import webdriver
from MainPage import MainPage

def test_calculator():
    delay = 45
    res = 15

    driver = webdriver.Chrome()
    main_page = MainPage(driver)    
    main_page.set_delay(delay)
    main_page.summator()
    assert float(main_page.summator_result(delay)) == res

    driver.close()