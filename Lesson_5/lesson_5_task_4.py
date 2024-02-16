#открыть страничку в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Трижды кликнуть по синей кнопке
for n in range(3):
    driver.get("http://uitestingplayground.com/dynamicid/")
    Add_Element = 'button.btn'
    click= driver.find_element(By.CSS_SELECTOR, Add_Element)
    click.send_keys(Keys.RETURN)
    sleep(1)

sleep(5)
driver.quit()


# открыть страницу в FireFox
from selenium import webdriver
driver = webdriver.Firefox()

# Трижды кликнуть по синей кнопке
for n in range(3):
    driver.get("http://uitestingplayground.com/dynamicid/")
    Add_Element = 'button.btn'
    click= driver.find_element(By.CSS_SELECTOR, Add_Element)
    click.send_keys(Keys.RETURN)
    sleep(1)

sleep(5)
driver.quit()