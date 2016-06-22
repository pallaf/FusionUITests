from selenium.webdriver.common.by import By
from tests.page.main_page import MainPage




class IndexPage(MainPage):

    backspace_click = (By.CSS_SELECTOR, '[ng-mousedown="keyClick(\'backspace\')"]')
    logout_button_click = (By.ID, 'logoutButton')

    def __init__(self, driver):
        super(IndexPage, self).__init__(driver)

    def navigate_to_index(self):
        self.open('http://192.168.10.3:8091/')
        return self

    def fill_by_click(self, _for_click):
        keys = list(_for_click)
        for i in keys:
            to_click = (By.CSS_SELECTOR, '[ng-mousedown="keyClick(%s)"]'%i)
            self.click(to_click)
            if keys[3] == i:
                self.click(self.backspace_click)
                self.click(to_click)
"""
    def logout(self):
        expected_value = 'language-string-ltr ng-isolate-scope'
        self.click(self.logout_button_click)

        text = self.driver.find_element(By.ID, 'LogonSlide').get_attribute('id')
        return expected_value, text
"""
