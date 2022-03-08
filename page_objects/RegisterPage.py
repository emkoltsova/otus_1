from selenium.webdriver.common.by import By

from .BasePage import BasePage


class RegisterPage(BasePage):
    REGISTER_PATH = '/index.php?route=account/register'
    PAGE_HEADER = (By.CSS_SELECTOR, "#content h1")
    HEADER_PERSONAL_DETAILS = (By.CSS_SELECTOR, "#account legend")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='firstname']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='lastname']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[name='telephone']")
    PASSWORD_HEADER = (By.CSS_SELECTOR, ".form-horizontal :nth-child(2) legend")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    PASS_CONFIRM_FIELD = (By.CSS_SELECTOR, "input[name='confirm']")
    LETTER_HEADER = (By.CSS_SELECTOR, ".form-horizontal :nth-child(3) legend")
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, ".radio-inline [value='0']")
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, ".radio-inline [value='1']")
    POLICY_CHECKBOX = (By.CSS_SELECTOR, "[name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[value='Continue']")
