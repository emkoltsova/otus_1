from selenium.webdriver.common.by import By


class RegisterPage:
    REGISTER_PATH = '/index.php?route=account/register'
    PAGE_HEADER = (By.CSS_SELECTOR, "h1")
    HEADER_PERSONAL_DETAILS = (By.CSS_SELECTOR, "#account legend")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='firstname']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='lastname']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[name='telephone']")
    PASSWORD_HEADER = (By.CSS_SELECTOR, ".form-horizontal :nth-child(2) legend")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    PASS_CONFIRM_FIELD = (By.CSS_SELECTOR, "input[name='confirm']")
    LETTER_HEADER = (By.CSS_SELECTOR, ".form-horizontal :nth-child(3) legend")
    RADIO_BUTTON = (By.CSS_SELECTOR, ".radio-inline [checked='checked']")
