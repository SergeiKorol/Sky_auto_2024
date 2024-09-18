from selenium.webdriver.common.by import By


class AuthPage:
    username = "standard_user"
    password = "secret_sauce"
    username_locator = "input#user-name"
    password_locator = "input#password"
    login_button = "input#login-button"

    def __init__(self, _driver):
        self._driver = _driver
        self._driver.maximize_window()
        self._driver.get("https://www.saucedemo.com/")

    def authorization(self):
        self._driver.find_element(By.CSS_SELECTOR, self.username_locator).send_keys(self.username)
        print('Input login')
        self._driver.find_element(By.CSS_SELECTOR, self.password_locator).send_keys(self.password)
        print('Input password')
        self._driver.find_element(By.CSS_SELECTOR, self.login_button).click()
        print('Click login button')
