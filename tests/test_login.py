from selenium import webdriver
from pages.login_page import loginpage
import time
def test(driver):
    login_page=loginpage(driver)

    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    login_page.login("standard_user","secret_sauce")
    time.sleep(2)
    driver.quit()


