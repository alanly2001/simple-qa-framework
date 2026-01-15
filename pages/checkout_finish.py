from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutFinish(BasePage):
    FINISH_BTN = (By.ID, "finish")
    
    def click_finish(self):
        self.driver.find_element(*self.FINISH_BTN).click()