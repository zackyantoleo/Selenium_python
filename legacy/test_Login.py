import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown(self):
    self.driver.quit()

  def test_Success_Login(self):        
      driver = self.driver
      driver.get("https://www.saucedemo.com/")
      
      driver.find_element(By.ID,"user-name").send_keys("standard_user")
      driver.find_element(By.ID,"password").send_keys("secret_sauce") 
      driver.find_element(By.ID, "login-button").click()
      time.sleep(1)
      elements = self.driver.find_elements(By.ID, "login-button")
      assert len(elements) == 0
      # driver.close()

  def test_Login_Invalid_Username_and_Password(self):
      driver = self.driver
      driver.get("https://www.saucedemo.com/")
      
      driver.find_element(By.ID,"user-name").send_keys("AAAAAAA")
      driver.find_element(By.ID,"password").send_keys("BBBBB") 
      driver.find_element(By.ID, "login-button").click()
      time.sleep(1)
      assert self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text == "Epic sadface: Username and password do not match any user in this service"


  def test_Case_Sensitivity_Test_Username_and_Password_Fields(self):
      driver = self.driver
      driver.get("https://www.saucedemo.com/")
      driver.find_element(By.ID,"user-name").send_keys("AAAAAAA")
      driver.find_element(By.ID,"password").send_keys("BBBBB") 
      driver.find_element(By.ID, "login-button").click()
      time.sleep(1)      
      assert self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text == "Epic sadface: Username and password do not match any user in this service"

  def test_Login_EmptyUser(self):
      driver = self.driver
      driver.get("https://www.saucedemo.com/")        
      driver.find_element(By.ID,"user-name").send_keys("")
      driver.find_element(By.ID,"password").send_keys("secret_sauce")
      driver.find_element(By.ID,"login-button").click()
      time.sleep(1)          
      assert self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text == "Epic sadface: Username is required"