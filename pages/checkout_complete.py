from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutComplete(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME = (By.ID, "back-to-products")
    
    def get_confirmation_text(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text
        
    def go_back_home(self):
        self.driver.find_element(*self.BACK_HOME).click()