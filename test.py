#Athif Zakiyanto
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    
    def setUp(self):
         self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_success_login(self):        
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce") 
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

    def test_b_login_invalid_username_and_password(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
        
        driver.find_element(By.ID,"user-name").send_keys("AAAAAAA")
        driver.find_element(By.ID,"password").send_keys("BBBBB") 
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        response_data = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        self.assertEqual(response_data, "Epic sadface: Username and password do not match any user in this service")

    def test_c_Login_EmptyUser(self):
        driver = self.browser
        driver.get("https://www.saucedemo.com/")
            
        driver.find_element(By.ID,"user-name").send_keys("")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
            
        response_data = driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button").text
        self.assertIn(response_data,"Username is required")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main() 