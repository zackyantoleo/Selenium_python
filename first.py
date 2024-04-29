import unittest
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_Success_Login(self):        
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
      
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce") 
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        elements = self.driver.find_elements(By.ID, "login-button")
        assert len(elements) == 0


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()