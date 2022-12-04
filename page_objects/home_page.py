from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class HomePage(BasePage):
    USER_MENU_ITEM = (By.ID, "header-menu-user")
    LOGOUT_BTN_ITEM = (By.ID, "menu-user-logout")

    def logout(self):
        menuBtn = self.wait_for(self.USER_MENU_ITEM)
        self.mouseHover(menuBtn)
        self.wait_for_clickable(self.LOGOUT_BTN_ITEM).click()