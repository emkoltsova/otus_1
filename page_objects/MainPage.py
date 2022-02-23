from selenium.webdriver.common.by import By


class MainPage:
    PAGE_HEADER = (By.CSS_SELECTOR, "#logo h1")
    CURRENCY_PICKER = (By.CSS_SELECTOR, ".dropdown-toggle .hidden-xs")
    SEARCH_FIELD = (By.CSS_SELECTOR, "[placeholder='Search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    CONTACT_PHONE = (By.CSS_SELECTOR, ".fa-phone")
    MACBOOK_IMAGE = (By.CSS_SELECTOR, "#slideshow0 :nth-child(3) [alt='MacBookAir']")
