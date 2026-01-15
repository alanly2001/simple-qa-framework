import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info import CheckoutInfoPage
from pages.checkout_finish import CheckoutFinish
from pages.checkout_complete import CheckoutComplete

def test_successful_checkout(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    inventory.go_to_cart()
    
    cart = CartPage(driver)
    time.sleep(5)
    cart.go_to_checkout()
    
    info = CheckoutInfoPage(driver)
    info.fill_checkout_info("A", "L", "12345")
    
    finish_checkout = CheckoutFinish(driver)
    finish_checkout.click_finish()
    
    complete_checkout = CheckoutComplete(driver)
    complete_checkout.get_confirmation_text()
    assert complete_checkout.get_confirmation_text() == "Thank you for your order!"
    complete_checkout.go_back_home()    