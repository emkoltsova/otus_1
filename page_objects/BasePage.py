from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def get_element_text(self, locator: tuple):
        return self.browser.find_element(*locator).text

    def fill_form(self, locator: tuple, text: str):
        self.browser.find_element(*locator).send_keys(text)

    def click_element(self, locator: tuple):
        ActionChains(self.browser).pause(2).move_to_element(self.browser.find_element(*locator)).click().perform()

    def get_elements(self, locator: tuple):
        self.verify_element_presence(locator)
        return self.browser.find_elements(*locator)

    def accept_alert(self):
        Alert(self.browser).accept()
