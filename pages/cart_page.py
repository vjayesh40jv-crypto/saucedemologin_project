from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class Cart:
    def __init__(self,driver):
        self.driver=driver
        self.cart1=(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
        self.cart2=(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        self.cart3=(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
        self.out=(By.ID,"react-burger-menu-btn")
        self.logout=(By.ID,"logout_sidebar_link")

    def product(self):
        self.driver.find_element(*self.cart1).click()
        self.driver.find_element(*self.cart2).click()
        self.driver.find_element(*self.cart3).click()

    def _logout(self):
        self.driver.find_element(*self.out).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout)).click()
