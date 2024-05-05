#Athif Zakiyanto
import pytest
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=options)

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()        
    
    def Success_Login(self):        
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce") 
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Products', response_data)
        # driver.close()

    def Login_Invalid_Username_and_Password(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        driver.find_element(By.ID,"user-name").send_keys("AAAAAAA")
        driver.find_element(By.ID,"password").send_keys("BBBBB") 
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        response_data = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        self.assertIn(response_data, "Epic sadface: Username and password do not match any user in this service")

    def Case_Sensitivity_Test_Username_and_Password_Fields(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID,"user-name").send_keys("AAAAAAA")
        driver.find_element(By.ID,"password").send_keys("BBBBB") 
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        response_data = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        self.assertIn(response_data, "Epic sadface: Username and password do not match any user in this service")

    def Login_EmptyUser(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
            
        driver.find_element(By.ID,"user-name").send_keys("")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
            
        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button").text
        self.assertIn(response_data,"Username is required")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()