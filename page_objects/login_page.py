from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class LoginPage(BasePage):   
    expected_title = 'Smartbear BitBar - App Testing on Real Android and iOS Devices'
    USERNAME_ITEM = (By.ID, "login-email")
    PASSWORD_ITEM = (By.ID, "login-password")
    LOGIN_BTN_ITEM = (By.ID, "login-submit")

    def __init__(self, driver, username, password):
        super().__init__(driver)
        self.username = username 
        self.password = password

    # login page is also starting page in all our tests, so we can visit it from here
    def visit(self):
        self.driver.get("https://cloud.bitbar.com") 
        self.wait_for_title(self.expected_title)
    
    def login(self):
        self.wait_for(self.USERNAME_ITEM).send_keys(self.username)
        self.find(self.PASSWORD_ITEM).send_keys(self.password)
        self.find(self.LOGIN_BTN_ITEM).click()