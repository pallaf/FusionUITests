from selenium import webdriver


class Browser:
    def __init__(self):
        self.driver = None

    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver

    def stop(self):
        self.driver.close()
