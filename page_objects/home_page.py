import time

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class HomePage(BasePage):
    USER_MENU_ITEM = (By.ID, "header-menu-user")
    LOGOUT_BTN_ITEM = (By.ID, "menu-user-logout")
    PROJECTS_BTN_ITEM = (By.ID, "menu-main-testing-projects")
    POPUP_ITEM = (By.ID, "pendo-guide-container")
    POPUP_CLOSE_BTN_ITEM = (By.XPATH, "//button[@aria-label='Close']")

    def logout(self):
        menuBtn = self.wait_for(self.USER_MENU_ITEM)
        self.mouse_hover(menuBtn)
        self.wait_for_clickable(self.LOGOUT_BTN_ITEM).click()

    def closePopup(self):
        time.sleep(5)
        popup = self.find_elements_list(self.POPUP_ITEM)
        if popup:
            self.find(self.POPUP_CLOSE_BTN_ITEM).click()

    def nav_to_projects_page(self):
        self.wait_for(self.PROJECTS_BTN_ITEM).click()