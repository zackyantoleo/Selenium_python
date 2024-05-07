import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Page.logout_object import logout_object


@pytest.fixture(scope="function")
def driver():
  driver = webdriver.Chrome()
  driver.get("https://www.saucedemo.com/")
  yield driver
  driver.quit()

class Test_Logout:
  def test_logout(self, driver):
    # self.logger.info("Test Logout")
    print("Test Logout")
    logout_obj = logout_object(driver, wait_time=10)
    logout_obj.enter_username()
    logout_obj.enter_password()
    logout_obj.click_login_button()
    logout_obj.click_menu()
    logout_obj.click_logout()
    logout_obj.element_visible(By.ID, "login-button")

