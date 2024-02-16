from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://uitestingplayground.com/textinput')
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(button)


