#открыть страничку в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Открыть окно
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

# Кликнуть по кнопке
#'div.modal-footer p'
#'//*[@id="modal"]/div[2]/div[3]/p'
button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer p")
button.click()

sleep(5)
driver.quit()
