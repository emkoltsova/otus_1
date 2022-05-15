from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ItemPage(BasePage):
    IPHONE_ITEM_PATH = '/index.php?route=product/product&product_id=40'
    ITEM_IMG = (By.CSS_SELECTOR, "img[title='iPhone']")
    ITEM_HEADER = (By.CSS_SELECTOR, "h1")
    QUANTITY_FIELD = (By.CSS_SELECTOR, "[name='quantity']")
    ADD_ITEM_BUTTON = (By.CSS_SELECTOR, "button#button-cart")
    DESCRIPTION_TAB = (By.CSS_SELECTOR, "[href='#tab-description']")
    REVIEWS_TAB = (By.CSS_SELECTOR, "[href='#tab-review']")
