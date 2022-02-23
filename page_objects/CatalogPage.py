from selenium.webdriver.common.by import By


class CatalogPage:
    DESKTOP_PATH = '/index.php?route=product/category&path=20'
    ITEM_LABEL = (
    By.CSS_SELECTOR, ".breadcrumb [href='https://demo.opencart.com/index.php?route=product/category&path=20']")
    ITEM_HEADER = (By.CSS_SELECTOR, "h2")
    DESCRIPTION_IMAGE = (By.CSS_SELECTOR, ".col-sm-2 img")
    DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".col-sm-10 p")
    REFINE_SEARCH = (By.CSS_SELECTOR, "h3")
    LIST_VIEW = (By.CSS_SELECTOR, "button#list-view")
    GRID_VIEW = (By.CSS_SELECTOR, "button#grid-view")
