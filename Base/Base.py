from selenium.webdriver.support.wait import WebDriverWait

from appium import webdriver
class Base:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_element(self, loc, text):
        el = self.find_element(loc)
        el.clear()
        el.send_keys(text)

    def if_element(self, loc):
        try:
            self.find_element(loc)
            return True

        except Exception as e:
            return False