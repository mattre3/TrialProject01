import os
import unittest
from datetime import datetime 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from page_objects.login_page import LoginPage


class BitbarSeleniumSample(unittest.TestCase):

    def setUp(self):
        self.username = "michalkorybutwisniowiecki123@gmail.com"
        self.password = "WiUgTgQl[nnEl"

        # pick the best way for automation to save screenshots 
        self.test_result = None 
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.screenshot_dir = os.getcwd() + '/screenshots/session-' + self.driver.session_id
        #os.mkdir(self.screenshot_dir)

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()

    def test_login(self):
        loginPage = LoginPage(self.driver, self.username, self.password)
        # I wrap this all in a try/except so I can save screenshots on failure
        try:
            print("test_login start")
            wait = WebDriverWait(self.driver, 10)
            actions = ActionChains(self.driver)
            
            # check page title
            self.driver.get("https://cloud.bitbar.com")
            expected_title = 'Smartbear BitBar - App Testing on Real Android and iOS Devices'
            wait.until(EC.title_is(expected_title))    
            #self.driver.save_screenshot(self.screenshot_dir + '/' + 'login_page.png')

            loginPage.login()

            # welcome to bitbar window might show up
            self.driver.implicitly_wait(10)
            if self.driver.find_elements(By.ID, "pendo-guide-container"):
                self.driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()

            #self.driver.save_screenshot(self.screenshot_dir + '/' + 'home_page.png')
            # log out 
            menuBtn = wait.until(EC.presence_of_element_located((By.ID, "header-menu-user")))
            actions.move_to_element(menuBtn)
            actions.perform()
            logOutBtn = wait.until(EC.element_to_be_clickable((By.ID, "menu-user-logout")))
            logOutBtn.click()
        except Exception:
            # take screenshot on failure
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            #self.driver.save_screenshot(self.screenshot_dir + '/error-' + timestamp + '.png')
            raise

    
    """def test_projects(self):
        try:
            print("test_projects start")
            wait = WebDriverWait(self.driver, 10)
            #actions = ActionChains(self.driver)
            
            #implement POM to reduce code duplication
            
        except Exception:
            # take screenshot on failure
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            self.driver.save_screenshot(self.screenshot_dir + '/error-' + timestamp + '.png')
            raise"""


if __name__ == "__main__":
    unittest.main()
