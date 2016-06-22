from selenium.webdriver.common.by import By
from tests.page.index_page import IndexPage
import tests.page.log_on_page
from tests.page.trip_log_on_menu_page import TripLogOnMenuPage


class DriverLogOnPage(IndexPage):

    _back_button = (By.CSS_SELECTOR, '[ng-mousedown="back()"]')
    _enter_button = (By.CSS_SELECTOR, '[ng-mousedown="keyClick(\'enter\')"]')
    # _title_text = (By.CSS_SELECTOR, '.title .ng-binding')
    _logout_button = (By.ID, 'logoutButton')
    _error_tile = (By.CSS_SELECTOR, '[id=errorTile]>[class=ng-binding]')


    def __init__(self, driver):
        super(DriverLogOnPage, self).__init__(driver)

    def logon(self, driver_id):
        if driver_id != '111112' and driver_id != '111118':
            self._fill_driver_id_field(driver_id)
            self.wait_until_text_alert_is_present(self._error_tile)
            return DriverLogOnPage(self.get_driver())
        else:
            self._fill_driver_id(driver_id)
            self.wait_until_is_clickable(self._logout_button)
            return TripLogOnMenuPage(self.get_driver())

    def _fill_driver_id_field(self, driver_id):
        self.fill_by_click(driver_id)
        self._enter()

    def _fill_driver_id(self, driver_id):
        self.fill_by_click(driver_id)
        self._enter()

    def back_to_log_on_page(self):
        self.click(self._back_button)
        return tests.page.log_on_page.LogOnPage(self.get_driver())

    def _enter(self):
         self.click(self._enter_button)


