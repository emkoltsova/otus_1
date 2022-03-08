from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    CURRENCY_PICKER = (By.CSS_SELECTOR, ".dropdown-toggle .hidden-xs")
    CURRENCY_LIST = (By.CSS_SELECTOR, "#top .btn-group .dropdown-menu")
    CURRENCY_EURO = (By.CSS_SELECTOR, "[name='EUR']")
    CURRENCY_POUND = (By.CSS_SELECTOR, "[name='GBP']")
    CURRENCY_DOLLAR = (By.CSS_SELECTOR, "[name='USD']")
    CURRENCY_SIGN = (By.CSS_SELECTOR, "button strong")
    CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    ITEMS_PRICE = (By.CSS_SELECTOR, ".price")
    SEARCH_FIELD = (By.CSS_SELECTOR, "[placeholder='Search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    CONTACT_PHONE = (By.CSS_SELECTOR, ".fa-phone")
    MACBOOK_IMAGE = (By.CSS_SELECTOR, "#slideshow0 :nth-child(3) [alt='MacBookAir']")
