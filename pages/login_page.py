from selenium.webdriver.common.by import By

class loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.username=(By.ID,'user-name')
        self.password=(By.ID,'password')
        self.submit=(By.ID,'login-button')

    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submit).click()
