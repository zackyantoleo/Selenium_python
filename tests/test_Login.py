import pytest
from selenium import webdriver
from Page.login_object import login_object
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

class Test_Login:
    def test_Login_With_Valid_Username_and_Password(self, driver):
        # self.logger.info("Test Login_With_Valid_Username_and_Password")
        print("Test Login_With_Valid_Username_and_Password")
        login_page = login_object(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        assert login_page.element_not_visible(By.ID, "login-button")

    def test_Login_Invalid_Username_and_Password(self, driver):
        # self.logger.info("Test Login_Invalid_Username_and_Password")
        print("Test Login_Invalid_Username_and_Password")
        login_page = login_object(driver)
        login_page.enter_username("AAAAAAA")
        login_page.enter_password("BBBBB")
        login_page.click_login_button()
        assert login_page.get_error_message(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3") == \
         "Epic sadface: Username and password do not match any user in this service"

    def test_Case_Sensitivity_Test_Username_and_Password_Fields(self, driver):
        # self.logger.info("Test Case_Sensitivity_Test_Username_and_Password_Fields")
        print("Test Case_Sensitivity_Test_Username_and_Password_Fields")
        login_page = login_object(driver)
        login_page.enter_username("STANDARD_USER")
        login_page.enter_password("SECRET_SAUCE")
        login_page.click_login_button()
        assert login_page.get_error_message(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3") == \
         "Epic sadface: Username and password do not match any user in this service"

    def test_Login_Empty_Field(self, driver):
        # self.logger.info("Test Login_Empty_Field")
        print("Test Login_Empty_Field")
        login_page = login_object(driver)
        login_page.enter_username("")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        assert login_page.get_error_message(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3") == \
         "Epic sadface: Username is required"
