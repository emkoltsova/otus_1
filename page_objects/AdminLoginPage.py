from selenium.webdriver.common.by import By

from .BasePage import BasePage


class AdminLoginPage(BasePage):
    ADMIN_PATH = '/admin'
    HEADER_TEXT = (By.CSS_SELECTOR, "h1.panel-title")
    USERNAME_FIELD = (By.CSS_SELECTOR, "[name='username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "[href*='route=common/forgotten']")

    def login_to_admin(self, login='user', password='bitnami'):
        self.fill_form(self.USERNAME_FIELD, login)
        self.fill_form(self.PASSWORD_FIELD, password)
        self.click_element(self.SUBMIT_BUTTON)
