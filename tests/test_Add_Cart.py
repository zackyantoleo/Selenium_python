import pytest
import time
from selenium import webdriver
from Page.cart_object import cart_object
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

class Test_Add_Cart:
  def test_cart(self, driver):
    # self.logger.info("Test Add Cart")
    print("Test Add Cart")
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"inventory-item-name\"]").click()
