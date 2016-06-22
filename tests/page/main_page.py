from selenium.webdriver.common.by import By
from tests.page.abstract_page import AbstractPage




class MainPage(AbstractPage):

    _driver_button = (By.CSS_SELECTOR, '[ng-mousedown = "vm.showDriverLogon()"]')
    _log_on_slide = ((By.ID, 'LogonSlide'))
    _driver_log_on_slide = ((By.ID, 'DriverLogonSlide'))
    _create_account_button = (By.ID, 'sign_up')
    _create_category_button = (By.ID, 'create_category')
    _create_topic_button = (By.ID, 'create_topic')
    _index_button = (By.ID, 'home')

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def navigate_to_index(self):
        self.open('http://192.168.10.3:8091/')
        return self

    def open_log_on_page(self):
        from tests.page.log_on_page import LogOnPage
        self.wait_until_is_clickable(self._driver_button)
        return LogOnPage(self.get_driver())

    def open_driver_log_on_page(self):
        from tests.page.driver_log_on_page import DriverLogOnPage
        self.click(self._driver_button)
        self.wait_until_is_clickable(self. _driver_log_on_slide)
        return DriverLogOnPage(self.get_driver())

    def open_trip_log_on_menu_page(self):
        from tests.page.trip_log_on_menu_page import TripLogOnMenuPage
        # self.click(self._driver_button)
        # self.wait_until_is_clickable(self. _driver_log_on_slide)
        return TripLogOnMenuPage(self.get_driver())

