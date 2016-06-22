from selenium.webdriver.common.by import By

from tests.page.main_page import MainPage


class LogOnPage(MainPage):

    _driver_button = (By.CSS_SELECTOR, '[ng-mousedown = "vm.showDriverLogon()"]')

    def __init__(self, driver):
        super(LogOnPage, self).__init__(driver)


