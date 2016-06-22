from selenium.webdriver.common.by import By
from tests.page.log_on_page import LogOnPage
from tests.page.main_page import MainPage


class TripLogOnMenuPage (MainPage):

    _logout_button = (By.ID, 'logoutButton')
    _title_text = (By.CSS_SELECTOR, '[id="L_title"] .ng-binding')
    _driver_button = (By.CSS_SELECTOR, '[ng-mousedown = "vm.showDriverLogon()"]')


    def __init__(self, driver):
        super(TripLogOnMenuPage, self).__init__(driver)

    def log_out(self):
        self.wait_until_is_clickable(self._logout_button)
        self.click(self._logout_button)
        self.wait_until_is_clickable(self._driver_button)
        expected_value = self.get_text_from_element(self._title_text)
        if expected_value != 'Log-on':
            print expected_value, 'something wrong with the selctors or UI, check it!'
        return LogOnPage(self.get_driver())
