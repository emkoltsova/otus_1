import random

import allure
import pytest

from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminPage import AdminPage
from page_objects.CatalogPage import CatalogPage
from page_objects.ItemPage import ItemPage
from page_objects.MainPage import MainPage
from page_objects.RegisterPage import RegisterPage


@allure.description("""Проверка наличия элементов на странице каталога""")
def test_catalog(browser):
    page = CatalogPage(browser)
    browser.open(CatalogPage.DESKTOP_PATH)
    page_elements = [CatalogPage.ITEM_LABEL,
                     CatalogPage.ITEM_HEADER, CatalogPage.DESCRIPTION_IMAGE,
                     CatalogPage.DESCRIPTION_TEXT, CatalogPage.REFINE_SEARCH, CatalogPage.LIST_VIEW,
                     CatalogPage.GRID_VIEW]
    for el in page_elements:
        page.verify_element_presence(el)


@allure.description("""Проверка наличия элементов на странице регистрации нового пользователя""")
def test_register_page(browser):
    page = RegisterPage(browser)
    browser.open(RegisterPage.REGISTER_PATH)
    page_elements = [RegisterPage.PAGE_HEADER, RegisterPage.HEADER_PERSONAL_DETAILS, RegisterPage.FIRST_NAME_FIELD,
                     RegisterPage.LAST_NAME_FIELD, RegisterPage.EMAIL_FIELD, RegisterPage.PHONE_FIELD,
                     RegisterPage.PASSWORD_HEADER, RegisterPage.PASSWORD_FIELD, RegisterPage.PASS_CONFIRM_FIELD,
                     RegisterPage.LETTER_HEADER, RegisterPage.RADIO_BUTTON_NO]
    for el in page_elements:
        page.verify_element_presence(el)


@allure.description("""Проверка наличия элементов на главной странице""")
def test_main_page(browser):
    page = MainPage(browser)
    browser.open()
    page_elements = [MainPage.SEARCH_FIELD, MainPage.SEARCH_BUTTON, MainPage.CONTACT_PHONE,
                     MainPage.CURRENCY_PICKER, MainPage.MACBOOK_IMAGE]
    for el in page_elements:
        page.verify_element_presence(el)


@allure.description("""Проверка наличия элементов на странице авторизации в раздел админитсратора""")
def test_admin_login_page(browser):
    page = AdminLoginPage(browser)
    browser.open(AdminLoginPage.ADMIN_PATH)
    page_elements = [AdminLoginPage.HEADER_TEXT, AdminLoginPage.USERNAME_FIELD, AdminLoginPage.PASSWORD_FIELD,
                     AdminLoginPage.FORGOTTEN_PASSWORD, AdminLoginPage.SUBMIT_BUTTON]
    for el in page_elements:
        page.verify_element_presence(el)


@allure.description("""Проверка наличия элементов на странице товаров""")
def test_item_page(browser):
    page = ItemPage(browser)
    browser.open(ItemPage.IPHONE_ITEM_PATH)
    page_elements = [ItemPage.ITEM_HEADER, ItemPage.ITEM_IMG, ItemPage.QUANTITY_FIELD, ItemPage.ADD_ITEM_BUTTON,
                     ItemPage.DESCRIPTION_TAB, ItemPage.REVIEWS_TAB]
    for el in page_elements:
        page.verify_element_presence(el)


@allure.description("""Добавление нового продукта в разделе администратора""")
def test_add_new_product(browser):
    browser.open(AdminLoginPage.ADMIN_PATH)
    AdminLoginPage(browser).login_to_admin()
    page = AdminPage(browser)
    page.click_element(AdminPage.CATALOG_MENU)
    page.click_element(AdminPage.PRODUCTS_MENU)
    assert page.get_element_text(AdminPage.PAGE_HEADER) == 'Products'
    page.click_element(AdminPage.ADD_PRODUCT_BTN)
    assert page.get_element_text(AdminPage.PANEL_TITLE) == 'Add Product'
    product_info = {
        'name': 'New test product!',
        'tag': 'testing_tag',
        'model': 'test_model_10',
        'price': 100500.12
    }
    create_product(browser, product_info)
    assert 'Success' in page.get_element_text(AdminPage.ALERT_SUCCESS)
    filter_product(browser, product_info['name'])


@allure.description("""Удаление продукта в разделе администратора""")
def test_delete_product(browser):
    browser.open(AdminLoginPage.ADMIN_PATH)
    AdminLoginPage(browser).login_to_admin()
    page = AdminPage(browser)
    page.click_element(AdminPage.CATALOG_MENU)
    page.click_element(AdminPage.PRODUCTS_MENU)
    page.click_element(AdminPage.ADD_PRODUCT_BTN)
    product_info = {
        'name': 'New product to delete',
        'tag': 'testing_tag_del',
        'model': 'test_model_del',
        'price': 35
    }
    create_product(browser, product_info)
    filter_product(browser, product_info['name'])
    page.click_element(AdminPage.CHECK_PRODUCT)
    page.click_element(AdminPage.DELETE_PRODUCT_BTN)
    page.accept_alert()
    assert 'Success' in page.get_element_text(AdminPage.ALERT_SUCCESS)


@allure.description("""Иземенение валюты через выпадающий список""")
@pytest.mark.parametrize('cur_button, cur_text, cur_sign', [(MainPage.CURRENCY_EURO, '€ Euro', '€'),
                                                            (MainPage.CURRENCY_POUND, '£ Pound Sterling', '£'),
                                                            (MainPage.CURRENCY_DOLLAR, '$ US Dollar', '$')])
def test_change_currency(browser, cur_button, cur_text, cur_sign):
    browser.open()
    page = MainPage(browser)
    page.click_element(MainPage.CURRENCY_PICKER)
    assert page.get_element_text(cur_button) == cur_text
    page.click_element(cur_button)
    assert page.get_element_text(MainPage.CURRENCY_SIGN) == cur_sign
    assert cur_sign in page.get_element_text(MainPage.CART_TOTAL)
    for el in page.get_elements(MainPage.ITEMS_PRICE):
        assert cur_sign in el.text


@allure.description("""Добавление нового пользователя""")
def test_user_register(browser):
    browser.open(RegisterPage.REGISTER_PATH)
    page = RegisterPage(browser)
    assert page.get_element_text(RegisterPage.PAGE_HEADER) == 'Register Account'
    page.fill_form(RegisterPage.FIRST_NAME_FIELD, 'test_first_name')
    page.fill_form(RegisterPage.LAST_NAME_FIELD, 'test_last_name')
    page.fill_form(RegisterPage.EMAIL_FIELD,
                   'test_user_' + str(random.randint(1, 10000)) + '@gmail.com')
    page.fill_form(RegisterPage.PHONE_FIELD, '89997775634')
    page.fill_form(RegisterPage.PASSWORD_FIELD, '1234567890')
    page.fill_form(RegisterPage.PASS_CONFIRM_FIELD, '1234567890')
    page.click_element(RegisterPage.RADIO_BUTTON_YES)
    page.click_element(RegisterPage.POLICY_CHECKBOX)
    page.click_element(RegisterPage.CONTINUE_BUTTON)
    assert page.get_element_text(RegisterPage.PAGE_HEADER) == 'Your Account Has Been Created!'


def create_product(browser, product: dict):
    page = AdminPage(browser)
    page.fill_form(AdminPage.PRODUCT_NAME_FIELD, product['name'])
    page.fill_form(AdminPage.TAG_TITLE_FIELD, product['tag'])
    page.click_element(AdminPage.DATA_TAB)
    page.fill_form(AdminPage.MODEL_FIELD, product['model'])
    page.fill_form(AdminPage.PRICE_FIELD, product['price'])
    page.click_element(AdminPage.SAVE_BTN)


def filter_product(browser, product_name):
    page = AdminPage(browser)
    page.fill_form(AdminPage.PRODUCT_NAME_FIELD, product_name)
    page.click_element(AdminPage.FILTER_BUTTON)
    assert product_name in page.get_element_text(AdminPage.TABLE_PRODUCT_NAME)
