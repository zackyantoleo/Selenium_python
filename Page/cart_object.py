from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class cart_object: 
    def __init__(self, driver, wait_time=6):
        self.driver = driver
        self.driver.implicitly_wait(wait_time)
        self.wait_time = wait_time

    def enter_username(self, username="standard_user"):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def click_logout(self):
        self.driver.find_element(By.ID, "logout-button").click()
   
    
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