from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login_object: 
    def __init__(self, driver, wait_time=6):
        self.driver = driver
        self.driver.implicitly_wait(wait_time)
        self.wait_time = wait_time

    def enter_username(self, username="standard_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)        

    def enter_password(self, password="secret_sauce"):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login-button").click()

    def login_button_invisibility(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.ID, "login-button")))
        except:
            return False
        return True        
    
    def element_visible(self, by, locator):
        try:
            WebDriverWait(self.driver, self.wait_time).until(EC.invisibility_of_element_located((by, locator)))
        except:
            return True
        return False  
    
    def element_not_visible(self, by, locator):
        try:
            WebDriverWait(self.driver, self.wait_time).until(EC.invisibility_of_element_located((by, locator)))
        except:
            return False
        return True

    def get_error_message(self, by, locator):
        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator)))
        return error_message.text