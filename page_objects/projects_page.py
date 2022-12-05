from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

from page_objects.base_page import BasePage


class ProjectsPage(BasePage):
    CREATE_PROJECT_ITEM = (By.XPATH, "//div[@title='Create new project']")
    PROJECT_NAME_INPUT_ITEM = (By.ID, "form-name")
    CREATE_PROJECT_BUTTON = (By.XPATH, "//button[@title='Create']")
    PROJECTS_LIST_ITEM = (By.CLASS_NAME, "project")
    FINAL_DELETE_BTN = (By.XPATH, "//button[@title='Delete']")

    def _close_project(self):
        open_project_xpath = "//div[@class='project opened']/div[@class='project-header']"
        OPEN_PROJECT_ITEM = (By.XPATH, open_project_xpath)
        # search for open project for a few seconds - return empty list if not found
        open_project_list = self.safe_wait_for(OPEN_PROJECT_ITEM)
        if open_project_list:
            self.click_stale_element(OPEN_PROJECT_ITEM)
    
    def create_new_project(self, project_name):
        self.click_stale_element(self.CREATE_PROJECT_ITEM)
        self.wait_for(self.PROJECT_NAME_INPUT_ITEM).send_keys(project_name)
        self.find(self.CREATE_PROJECT_BUTTON).click()

    def delete_project(self, project_name):
        self._close_project()

        project_xpath = f"//span[text()='{project_name}']//ancestor::div[@class='project']"
        project_options_xpath = project_xpath + "//descendant::div[@title='Options']"
        remove_project_btn_xpath = project_options_xpath + "//descendant::li[@title='Remove']"
        PROJECT_OPTIONS_ITEM = (By.XPATH, project_options_xpath)
        PROJECT_REMOVE_BTN = (By.XPATH, remove_project_btn_xpath)

        self.click_stale_element(PROJECT_OPTIONS_ITEM)
        self.wait_for_clickable(PROJECT_REMOVE_BTN).click()
        self.wait_for_clickable(self.FINAL_DELETE_BTN).click()

    def find_project(self, project_name):
        project_xpath = f"//span[text()='{project_name}']//ancestor::div[@class='project']"
        PROJECT_ITEM = (By.XPATH, project_xpath)
        return self.safe_wait_for(PROJECT_ITEM)
