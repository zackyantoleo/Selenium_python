import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogout:
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_logout(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(2)
    elements = self.driver.find_elements(By.ID, "login-button")    
    assert len(elements) > 0