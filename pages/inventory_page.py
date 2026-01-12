from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_BACKPACK_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TSHIRT_TO_CART = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    def add_item_to_cart(self):
        self.driver.find_element(*self.ADD_BACKPACK_TO_CART).click()
        self.driver.find_element(*self.ADD_TSHIRT_TO_CART).click()
        
    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text