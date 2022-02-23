from selenium.webdriver.common.by import By


class AdminLoginPage:
    ADMIN_PATH = '/admin'
    HEADER_TEXT = (By.CSS_SELECTOR, "h1.panel-title")
    USERNAME_FIELD = (By.CSS_SELECTOR, "[name='username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, "[href='https://demo.opencart.com/admin/index.php?route=common/forgotten']")
