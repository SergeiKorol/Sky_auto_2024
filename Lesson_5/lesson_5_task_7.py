#открыть страничку в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Открыть ссылку

driver.get("http://the-internet.herokuapp.com/inputs")
Element = 'input'
# Вписать 1000
click = driver.find_element(By.CSS_SELECTOR, Element)
click.send_keys("1000")
sleep(2)
click.clear()
sleep(2)
# Вписать 999
click = driver.find_element(By.CSS_SELECTOR, Element)
click.send_keys("999")

sleep(2)
driver.quit()