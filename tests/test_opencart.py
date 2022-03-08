import random

import pytest

from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminPage import AdminPage
from page_objects.CatalogPage import CatalogPage
from page_objects.ItemPage import ItemPage
from page_objects.MainPage import MainPage
from page_objects.RegisterPage import RegisterPage


def test_catalog(browser):
    browser.open(CatalogPage.DESKTOP_PATH)
    page_elements = [CatalogPage.ITEM_LABEL, CatalogPage.ITEM_HEADER, CatalogPage.DESCRIPTION_IMAGE,
                     CatalogPage.DESCRIPTION_TEXT, CatalogPage.REFINE_SEARCH, CatalogPage.LIST_VIEW,
                     CatalogPage.GRID_VIEW]
    for el in page_elements:
        CatalogPage(browser).verify_element_presence(el)


def test_register_page(browser):
    browser.open(RegisterPage.REGISTER_PATH)
    page_elements = [RegisterPage.PAGE_HEADER, RegisterPage.HEADER_PERSONAL_DETAILS, RegisterPage.FIRST_NAME_FIELD,
                     RegisterPage.LAST_NAME_FIELD, RegisterPage.EMAIL_FIELD, RegisterPage.PHONE_FIELD,
                     RegisterPage.PASSWORD_HEADER, RegisterPage.PASSWORD_FIELD, RegisterPage.PASS_CONFIRM_FIELD,
                     RegisterPage.LETTER_HEADER, RegisterPage.RADIO_BUTTON_NO]
    for el in page_elements:
        RegisterPage(browser).verify_element_presence(el)


def test_main_page(browser):
    browser.open()
    page_elements = [MainPage.SEARCH_FIELD, MainPage.SEARCH_BUTTON, MainPage.CONTACT_PHONE,
                     MainPage.CURRENCY_PICKER, MainPage.MACBOOK_IMAGE]
    for el in page_elements:
        MainPage(browser).verify_element_presence(el)


def test_admin_login_page(browser):
    browser.open(AdminLoginPage.ADMIN_PATH)
    page_elements = [AdminLoginPage.HEADER_TEXT, AdminLoginPage.USERNAME_FIELD, AdminLoginPage.PASSWORD_FIELD,
                     AdminLoginPage.FORGOTTEN_PASSWORD, AdminLoginPage.SUBMIT_BUTTON]
    for el in page_elements:
        AdminLoginPage(browser).verify_element_presence(el)


def test_item_page(browser):
    browser.open(ItemPage.IPHONE_ITEM_PATH)
    page_elements = [ItemPage.ITEM_HEADER, ItemPage.ITEM_IMG, ItemPage.QUANTITY_FIELD, ItemPage.ADD_ITEM_BUTTON,
                     ItemPage.DESCRIPTION_TAB, ItemPage.REVIEWS_TAB]
    for el in page_elements:
        ItemPage(browser).verify_element_presence(el)


def test_add_new_product(browser):
    browser.open(AdminLoginPage.ADMIN_PATH)
    AdminLoginPage(browser).login_to_admin()
    AdminPage(browser).click_element(AdminPage.CATALOG_MENU)
    AdminPage(browser).click_element(AdminPage.PRODUCTS_MENU)
    assert AdminPage(browser).get_element_text(AdminPage.PAGE_HEADER) == 'Products'
    AdminPage(browser).click_element(AdminPage.ADD_PRODUCT_BTN)
    assert AdminPage(browser).get_element_text(AdminPage.PANEL_TITLE) == 'Add Product'
    product_info = {
        'name': 'New test product!',
        'tag': 'testing_tag',
        'model': 'test_model_10',
        'price': 100500.12
    }
    create_product(browser, product_info)
    assert 'Success' in AdminPage(browser).get_element_text(AdminPage.ALERT_SUCCESS)
    filter_product(browser, product_info['name'])


def test_delete_product(browser):
    browser.open(AdminLoginPage.ADMIN_PATH)
    AdminLoginPage(browser).login_to_admin()
    AdminPage(browser).click_element(AdminPage.CATALOG_MENU)
    AdminPage(browser).click_element(AdminPage.PRODUCTS_MENU)
    AdminPage(browser).click_element(AdminPage.ADD_PRODUCT_BTN)
    product_info = {
        'name': 'New product to delete',
        'tag': 'testing_tag_del',
        'model': 'test_model_del',
        'price': 35
    }
    create_product(browser, product_info)
    filter_product(browser, product_info['name'])
    AdminPage(browser).click_element(AdminPage.CHECK_PRODUCT)
    AdminPage(browser).click_element(AdminPage.DELETE_PRODUCT_BTN)
    AdminPage(browser).accept_alert()
    assert 'Success' in AdminPage(browser).get_element_text(AdminPage.ALERT_SUCCESS)


@pytest.mark.parametrize('currency', ['EURO', 'POUND', 'DOLLAR'])
def test_change_currency(browser, currency):
    browser.open()
    MainPage(browser).click_element(MainPage.CURRENCY_PICKER)
    if currency == 'EURO':
        cur_button = MainPage.CURRENCY_EURO
        cur_text = '€ Euro'
        cur_sign = '€'
    elif currency == 'POUND':
        cur_button = MainPage.CURRENCY_POUND
        cur_text = '£ Pound Sterling'
        cur_sign = '£'
    elif currency == 'DOLLAR':
        cur_button = MainPage.CURRENCY_DOLLAR
        cur_text = '$ US Dollar'
        cur_sign = '$'
    assert MainPage(browser).get_element_text(cur_button) == cur_text
    MainPage(browser).click_element(cur_button)
    assert MainPage(browser).get_element_text(MainPage.CURRENCY_SIGN) == cur_sign
    assert cur_sign in MainPage(browser).get_element_text(MainPage.CART_TOTAL)
    for el in MainPage(browser).get_elements(MainPage.ITEMS_PRICE):
        assert cur_sign in el.text


def test_user_register(browser):
    browser.open(RegisterPage.REGISTER_PATH)
    assert RegisterPage(browser).get_element_text(RegisterPage.PAGE_HEADER) == 'Register Account'
    RegisterPage(browser).fill_form(RegisterPage.FIRST_NAME_FIELD, 'test_first_name')
    RegisterPage(browser).fill_form(RegisterPage.LAST_NAME_FIELD, 'test_last_name')
    RegisterPage(browser).fill_form(RegisterPage.EMAIL_FIELD,
                                    'test_user_' + str(random.randint(1, 10000)) + '@gmail.com')
    RegisterPage(browser).fill_form(RegisterPage.PHONE_FIELD, '89997775634')
    RegisterPage(browser).fill_form(RegisterPage.PASSWORD_FIELD, '1234567890')
    RegisterPage(browser).fill_form(RegisterPage.PASS_CONFIRM_FIELD, '1234567890')
    RegisterPage(browser).click_element(RegisterPage.RADIO_BUTTON_YES)
    RegisterPage(browser).click_element(RegisterPage.POLICY_CHECKBOX)
    RegisterPage(browser).click_element(RegisterPage.CONTINUE_BUTTON)
    assert RegisterPage(browser).get_element_text(RegisterPage.PAGE_HEADER) == 'Your Account Has Been Created!'


def create_product(browser, product: dict):
    AdminPage(browser).fill_form(AdminPage.PRODUCT_NAME_FIELD, product['name'])
    AdminPage(browser).fill_form(AdminPage.TAG_TITLE_FIELD, product['tag'])
    AdminPage(browser).click_element(AdminPage.DATA_TAB)
    AdminPage(browser).fill_form(AdminPage.MODEL_FIELD, product['model'])
    AdminPage(browser).fill_form(AdminPage.PRICE_FIELD, product['price'])
    AdminPage(browser).click_element(AdminPage.SAVE_BTN)


def filter_product(browser, product_name):
    AdminPage(browser).fill_form(AdminPage.PRODUCT_NAME_FIELD, product_name)
    AdminPage(browser).click_element(AdminPage.FILTER_BUTTON)
    assert product_name in AdminPage(browser).get_element_text(AdminPage.TABLE_PRODUCT_NAME)
