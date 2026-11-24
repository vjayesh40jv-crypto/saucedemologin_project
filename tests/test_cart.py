from selenium import webdriver
from pages.cart_page import Cart
from pages.login_page import loginpage
import time
def test(driver):
    login_page=loginpage(driver)
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    assert(driver.current_url == "https://www.saucedemo.com/inventory.html")
    cart_page=Cart(driver)
    time.sleep(2)
    cart_page.product()
    cart_page._logout()
    time.sleep(2)