#открыть страничку в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/login")

login = 'input#username'
click= driver.find_element(By.CSS_SELECTOR, login)
click.send_keys("tomsmith")

password = 'input#password'
click= driver.find_element(By.CSS_SELECTOR, password)
click.send_keys("SuperSecretPassword!")

click= driver.find_element(By.CSS_SELECTOR, 'i.fa')
click.click()
sleep(2)
driver.quit()