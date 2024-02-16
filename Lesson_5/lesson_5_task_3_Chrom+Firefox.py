#открыть страничку в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")


Add_Element = "//button[contains(text(),'Add Element')]"
button = driver.find_element(By.XPATH, Add_Element)

# кликнуть на кнопку Add Element 5 раз

for n in range(5):
    button.click()
    sleep(1)
sleep(5)

#собрать со странички список кнопок Delete

delete_button = driver.find_elements(By.XPATH, '//button[contains(text(),"Delete")]')

#вывести на экран размер списка
print("Размер списка", {len(delete_button)})
driver.quit()



# открыть страницу в FireFox
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
Add_Element = "//button[contains(text(),'Add Element')]"
button = driver.find_element(By.XPATH, Add_Element)

# кликнуть на кнопку Add Element 5 раз

for n in range(5):
    button.click()
    sleep(1)
sleep(5)

#собрать со странички список кнопок

delete_button = driver.find_elements(By.XPATH, '//button[contains(text(),"Delete")]')


#вывести на экран размер списка
print("Размер списка", {len(delete_button)})
driver.quit()

