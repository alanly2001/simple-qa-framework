from pages.login_page import LoginPage

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("invalid_user", "invalid_pass")
    
    assert "Epic sadface" in driver.page_source