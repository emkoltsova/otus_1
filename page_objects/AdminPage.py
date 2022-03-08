from selenium.webdriver.common.by import By

from .BasePage import BasePage


class AdminPage(BasePage):
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS_MENU = (By.CSS_SELECTOR, "#menu-catalog li:nth-child(2)")
    PAGE_HEADER = (By.CSS_SELECTOR, "h1")
    ADD_PRODUCT_BTN = (By.CSS_SELECTOR, "[data-original-title='Add New']")
    DELETE_PRODUCT_BTN = (By.CSS_SELECTOR, "[data-original-title='Delete']")
    SAVE_BTN = (By.CSS_SELECTOR, "[data-original-title='Save']")
    PANEL_TITLE = (By.CSS_SELECTOR, ".panel-title")
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, "[placeholder='Product Name']")
    TAG_TITLE_FIELD = (By.CSS_SELECTOR, "[placeholder='Meta Tag Title']")
    DATA_TAB = (By.CSS_SELECTOR, "[href='#tab-data']")
    MODEL_FIELD = (By.CSS_SELECTOR, "[placeholder='Model']")
    PRICE_FIELD = (By.CSS_SELECTOR, "[placeholder='Price']")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#button-filter")
    TABLE_PRODUCT_NAME = (By.CSS_SELECTOR, "tbody td:nth-child(3)")
    CHECK_PRODUCT = (By.CSS_SELECTOR, "tbody [type='checkbox']")
