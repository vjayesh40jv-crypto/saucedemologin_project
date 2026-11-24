
import pytest
from selenium import webdriver



@pytest.fixture
def driver():
    print("TEST STARTS....")
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    print("TEST ENDS....")

    driver.quit()


