from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AbstractPage(object):
    def __init__(self, driver):
        self._driver = driver

    def get_driver(self):
        return self._driver

    def open(self, url):
        self._driver.get(url)

    def find_element(self, locator):
        return self.get_driver().find_element(*locator)

    def find_elements(self, locator):
        return self.get_driver().find_elements(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def wait(self, locator):
        WebDriverWait(self.get_driver(), 10).until(locator)

    def wait_until_is_clickable(self, locator):
        self.wait(EC.element_to_be_clickable(locator))

    def wait_until_element_is_invisible(self, locator):
        self.wait(EC.invisibility_of_element_located(locator))

    def wait_until_element_is_present(self, locator):
        self.wait(EC.presence_of_element_located(locator))

    def wait_until_text_is_present(self, locator, text):
        self.wait(EC.text_to_be_present_in_element(locator, text))

    def wait_until_is_visible(self, locator):
        self.wait(EC._element_if_visible(locator))

    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    def get_text_from_elements(self, list_locator):
        return [element.text for element in self.find_elements(list_locator)]

    def get_page_source(self):
        return self.get_driver().page_source

    def get_attribute_value(self, locator, attr):
        self.find_element(locator).get_attribute(attr)

    def wait_until_text_alert_is_present(self, locator):
        is_text_appeared = False
        while not is_text_appeared:
                text = self.get_text_from_element(locator)
                if len(text) > 0:
                    is_text_appeared = True



