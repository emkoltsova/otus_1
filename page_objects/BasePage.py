import logging

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        fh = logging.FileHandler('./test_opencart.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step("Проверка наличия элемента {locator} на странице.")
    def verify_element_presence(self, locator: tuple):
        self.logger.info("Check if element {} is present".format(locator))
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(name=self.browser.session_id,
                          body=self.browser.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG
                          )
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Получаем текст элемента {locator}.")
    def get_element_text(self, locator: tuple):
        self.logger.info("Get text of the element: {}".format(locator))
        return self.browser.find_element(*locator).text

    @allure.step("Заполняем поле {locator}.")
    def fill_form(self, locator: tuple, text: str):
        self.logger.info("Input {} in input {}".format(text, locator))
        self.browser.find_element(*locator).send_keys(text)

    @allure.step("Клик по полю {locator}.")
    def click_element(self, locator: tuple):
        self.logger.info("Clicking element: {}".format(locator))
        ActionChains(self.browser).pause(2).move_to_element(self.browser.find_element(*locator)).click().perform()

    @allure.step("Получение всех элементов по локатору {locator}.")
    def get_elements(self, locator: tuple):
        self.logger.info("Get all elements by locator: {}".format(locator))
        self.verify_element_presence(locator)
        return self.browser.find_elements(*locator)

    @allure.step("Подтверждение алерта.")
    def accept_alert(self):
        self.logger.info("Accept alert")
        Alert(self.browser).accept()
