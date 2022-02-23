from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.CatalogPage import CatalogPage
from page_objects.ItemPage import ItemPage
from page_objects.MainPage import MainPage
from page_objects.RegisterPage import RegisterPage


def test_main_page_menu(browser):
    browser.find_element(*MainPage.PAGE_HEADER)
    browser.find_element(*MainPage.SEARCH_FIELD)
    browser.find_element(*MainPage.SEARCH_BUTTON)
    browser.find_element(*MainPage.CONTACT_PHONE)
    browser.find_element(*MainPage.CURRENCY_PICKER)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(MainPage.MACBOOK_IMAGE))


def test_catalog(browser):
    browser.get(browser.url + CatalogPage.DESKTOP_PATH)
    browser.find_element(*CatalogPage.ITEM_LABEL)
    browser.find_element(*CatalogPage.ITEM_HEADER)
    browser.find_element(*CatalogPage.DESCRIPTION_IMAGE)
    browser.find_element(*CatalogPage.DESCRIPTION_TEXT)
    browser.find_element(*CatalogPage.REFINE_SEARCH)
    browser.find_element(*CatalogPage.LIST_VIEW)
    browser.find_element(*CatalogPage.GRID_VIEW)


def test_register_page(browser):
    browser.get(browser.url + RegisterPage.REGISTER_PATH)
    browser.find_element(*RegisterPage.PAGE_HEADER)
    browser.find_element(*RegisterPage.HEADER_PERSONAL_DETAILS)
    browser.find_element(*RegisterPage.FIRST_NAME_FIELD)
    browser.find_element(*RegisterPage.LAST_NAME_FIELD)
    browser.find_element(*RegisterPage.EMAIL_FIELD)
    browser.find_element(*RegisterPage.PHONE_FIELD)
    browser.find_element(*RegisterPage.PASSWORD_HEADER)
    browser.find_element(*RegisterPage.PASSWORD_FIELD)
    browser.find_element(*RegisterPage.PASS_CONFIRM_FIELD)
    browser.find_element(*RegisterPage.LETTER_HEADER)
    browser.find_element(*RegisterPage.RADIO_BUTTON)


def test_admin_login_page(browser):
    browser.get(browser.url + AdminLoginPage.ADMIN_PATH)
    browser.find_element(*AdminLoginPage.HEADER_TEXT)
    browser.find_element(*AdminLoginPage.USERNAME_FIELD)
    browser.find_element(*AdminLoginPage.PASSWORD_FIELD)
    browser.find_element(*AdminLoginPage.FORGOTTEN_PASSWORD)
    browser.find_element(*AdminLoginPage.SUBMIT_BUTTON)


def test_item_page(browser):
    browser.get(browser.url + ItemPage.IPHONE_ITEM_PATH)
    browser.find_element(*ItemPage.ITEM_HEADER)
    browser.find_element(*ItemPage.ITEM_IMG)
    browser.find_element(*ItemPage.QUANTITY_FIELD)
    browser.find_element(*ItemPage.ADD_ITEM_BUTTON)
    browser.find_element(*ItemPage.DESCRIPTION_TAB)
    browser.find_element(*ItemPage.REVIEWS_TAB)
