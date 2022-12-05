import os
import unittest
import random 
import string 
from datetime import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.projects_page import ProjectsPage


class BitbarSeleniumTest(unittest.TestCase):

    def setUp(self):
        self.username = "michalkorybutwisniowiecki123@gmail.com"
        self.password = "WiUgTgQl[nnEl"
        self.screenshot_dir = os.getcwd() + '/screenshots'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()

    def _generateProjectName(self):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(10))
        return result_str

    def test_login(self):
        try:
            loginPage = LoginPage(self.driver, self.username, self.password)
            loginPage.visit()
            loginPage.login()

            homePage = HomePage(self.driver)
            # welcome to bitbar window might show up
            homePage.closePopup()
            homePage.logout()

        except Exception:
            timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            self.driver.save_screenshot(self.screenshot_dir + '/test_login-error-' + timestamp + '.png')
            raise

    
    def test_projects(self):
        try:
            project_name_list = []

            loginPage = LoginPage(self.driver, self.username, self.password)
            loginPage.visit()
            loginPage.login()

            homePage = HomePage(self.driver)
            # welcome to bitbar window might show up
            homePage.closePopup()
            homePage.nav_to_projects_page()

            projectsPage = ProjectsPage(self.driver)
            for i in range(3):
                project_name = self._generateProjectName()
                project_name_list.append(project_name)
                projectsPage.create_new_project(project_name)

            project_name_list.sort(reverse=True)
            for project_name in project_name_list:
                projectsPage.delete_project(project_name)
            
            # final check if all projects were successfully deleted
            self.assertTrue(projectsPage.find_project("Android Demo Project"))
            
        except Exception:
            timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            self.driver.save_screenshot(self.screenshot_dir + '/test_project-error-' + timestamp + '.png')
            raise

if __name__ == "__main__":
    unittest.main()
