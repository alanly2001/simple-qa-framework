from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_to_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    
    assert inventory.get_cart_count() == "2"