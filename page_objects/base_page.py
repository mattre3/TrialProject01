from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

import time

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # custom wait - returns empty list if it doesn't find element
    def safe_wait_for(self, locator):
        for i in range(3):
            element_list = self.find_elements_list(locator)
            if element_list:
                return element_list
            time.sleep(1)
        return []
    
    # Stale Element Exception handler
    def click_stale_element(self, locator):
        try:
            self.wait_for_clickable(locator).click()
        except StaleElementReferenceException:
            time.sleep(1)
            self.click_stale_element(locator)

    def wait_for_title(self, expected_title):
        return self.wait.until(EC.title_is(expected_title))

    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements_list(self, locator):
        return self.driver.find_elements(*locator)

    def mouse_hover(self, element):
        self.actions.move_to_element(element)
        self.actions.perform()


