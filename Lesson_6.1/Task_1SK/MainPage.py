from selenium.webdriver.common.by import By
from test_data import *


class MainPage:
    def __init__(self, driver):
        self._driver = driver
    # Локаторы для основной страницы    
    first_name_locator = "input[name='first-name']"
    last_name_locator = "input[name='last-name']"
    address_locator = "input[name='address']"
    email_locator = "input[name='e-mail']"
    phone_locator = "input[name='phone']"
    zip_locator = "input[name='zip-code']"
    city_locator = "input[name='city']"
    country_locator = "input[name='country']"
    job_locator = "input[name='job-position']"
    company_locator = "input[name='company']"
    submit_button = "button[type='submit']"
    web_elements = ""
    red_color = "rgba(132, 32, 41, 1)"
    green_color = "rgba(15, 81, 50, 1)"
    URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def fill_fields(self):
        self._driver.find_element(By.CSS_SELECTOR, self.first_name_locator).send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, self.last_name_locator).send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, self.address_locator).send_keys(address)
        self._driver.find_element(By.CSS_SELECTOR, self.email_locator).send_keys(email)
        self._driver.find_element(By.CSS_SELECTOR, self.phone_locator).send_keys(phone)
        self._driver.find_element(By.CSS_SELECTOR, self.zip_locator).send_keys(zip)
        self._driver.find_element(By.CSS_SELECTOR, self.city_locator).send_keys(city)
        self._driver.find_element(By.CSS_SELECTOR, self.country_locator).send_keys(country)
        self._driver.find_element(By.CSS_SELECTOR, self.job_locator).send_keys(job)
        self._driver.find_element(By.CSS_SELECTOR, self.company_locator).send_keys(company)

    def is_first_name(self):
        first_name_color = self.web_elements[3].find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
        if first_name_color == self.green_color:
            return True
    
    def is_last_name(self):
        last_name_color = self.web_elements[3].find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")
        if last_name_color == self.green_color:
            return True

    def is_address(self):
        address_color = self.web_elements[4].find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")
        if address_color == self.green_color:
            return True
        
    def is_email(self):
        email_color = self.web_elements[5].find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")
        if email_color == self.green_color:
            return True

    def is_phone(self):
        phone_color = self.web_elements[5].find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")
        if phone_color == self.green_color:
            return True

    def is_zip(self):
        zip_color = self.web_elements[4].find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
        if zip_color == self.red_color:
            return True
 
    def is_city(self):
        city_color = self.web_elements[4].find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")
        if city_color == self.green_color:
            return True

    def is_country(self):
        country_color = self.web_elements[4].find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")
        if country_color == self.green_color:
            return True
        
    def is_job(self):
        job_color = self.web_elements[6].find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")
        if job_color == self.green_color:
            return True

    def is_company(self):
        company_color = self.web_elements[6].find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")
        if company_color == self.green_color:
            return True
        
    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, self.submit_button).click()
        self.web_elements = self._driver.find_elements(By.CSS_SELECTOR, "div.row")   
            

    