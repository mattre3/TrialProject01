from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoginPage(BasePage):   
    expected_title = 'Smartbear BitBar - App Testing on Real Android and iOS Devices'
    username_selector = (By.ID, "login-email")
    password_selector = (By.ID, "login-password")
    login_btn_selector = (By.ID, "login-submit")

    def __init__(self, driver, username, password):
        super().__init__(driver)
        self.username = username 
        self.password = password
    
    def login(self):
        self.wait_for(self.username_selector).send_keys(self.username)
        self.find(self.password_selector).send_keys(self.password)
        self.find(self.login_btn_selector).click()