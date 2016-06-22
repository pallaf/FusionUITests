import unittest
from hamcrest import assert_that, contains_string
from tests.browser import Browser
from tests.page.index_page import IndexPage


class DriverLogInTest(unittest.TestCase):
    def setUp(self):
        self.browser = Browser()
        self.driver = self.browser.start()

    def test_driver_logging_in_should_succeed_with_logging_out(self):
        # given
        driver_id = '1'

        # when
        index_page = IndexPage(self.driver).navigate_to_index()
        log_on_page = index_page.open_log_on_page()
        driver_log_on_page = log_on_page.open_driver_log_on_page()
        post_trip_log_on_menu_page = driver_log_on_page.logon(driver_id)

        # then
        # expected_value = 'Trip log-on'
        expected_value = 'Fahrtauswahl'
        assert_that(post_trip_log_on_menu_page.get_page_source(), contains_string(expected_value))
        trip_log_on_menu_page = index_page.open_trip_log_on_menu_page()
        Post_Log_On_Page = trip_log_on_menu_page.log_out()
        expected_value = 'Anmeldung'
        assert_that(Post_Log_On_Page.get_page_source(), contains_string(expected_value))

    def test_driver_logging_in_should_succeed(self):
        # given
        driver_id = '111118'

        # when
        index_page = IndexPage(self.driver).navigate_to_index()
        log_on_page = index_page.open_log_on_page()
        driver_log_on_page = log_on_page.open_driver_log_on_page()
        post_trip_log_on_menu_page = driver_log_on_page.logon(driver_id)

        # then
        expected_value = 'Trip log-on'
        assert_that(post_trip_log_on_menu_page.get_page_source(), contains_string(expected_value))

    def test_driver_logging_in_should_not_succeed_with_invalid_id(self):
        # given
        driver_id = '000000'

        # when
        index_page = IndexPage(self.driver).navigate_to_index()
        log_on_page = index_page.open_log_on_page()
        driver_log_on_page = log_on_page.open_driver_log_on_page()
        post_driver_log_on_page = driver_log_on_page.logon(driver_id)

        # then
        # expected_value = 'No data supply'
        expected_value = 'Invalid BC-ID!'
        assert_that(post_driver_log_on_page.get_page_source(), contains_string(expected_value))

    def tearDown(self):
        self.browser.stop()