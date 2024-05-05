import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_Login_With_Valid_Usernae_and_Password(driver):
    print("Login_With_Valid_Usernae_and_Password")  
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce") 
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.ID, "login-button")))
    assert not driver.find_elements(By.ID, "login-button")

def test_Login_Invalid_Username_and_Password(driver):
    print("Login_With_Invalid_Usernae_and_Password")
    driver.find_element(By.ID,"user-name").send_keys("AAAAAAA")
    driver.find_element(By.ID,"password").send_keys("BBBBB") 
    driver.find_element(By.ID, "login-button").click()
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

def test_Case_Sensitivity_Test_Username_and_Password_Fields(driver):
    print("Case_Sensitivity_Test_Username_and_Password_Fields")
    driver.find_element(By.ID,"user-name").send_keys("AAAAAAA")
    driver.find_element(By.ID,"password").send_keys("BBBBB") 
    driver.find_element(By.ID, "login-button").click()
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

def test_Login_Empty_Field(driver):
    print("Case_Sensitivity_Test_Username_and_Password_Fields")
    driver.find_element(By.ID,"user-name").send_keys("")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    error_message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
    assert error_message.text == "Epic sadface: Username is required"
