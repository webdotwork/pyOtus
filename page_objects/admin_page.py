from selenium.webdriver.common.by import By
from helpers import random_string, random_email
from page_objects.base_page import BasePage

class AdminPage(BasePage):
    INPUT_NAME = (By.CSS_SELECTOR, "input[name='username']")
    INPUT_PASSWD = (By.CSS_SELECTOR, "input[name='password']")
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog > a")
    PRODUCTS = (By.CSS_SELECTOR, "#collapse-1 > li:nth-child(2) > a")
    ADD_PRODUCT = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a")
    CLICL_CAT = (By.CSS_SELECTOR, "#language-1 > div:nth-child(1) > div")
    INPUT_CATEGORY = (By.CSS_SELECTOR, "#input-name-1")
    INPUT_TAG = (By.CSS_SELECTOR, "input[id='input-meta-title-1']")
    CLICK_DATA = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a")
    INPUT_MODEl = (By.CSS_SELECTOR, "input[id='input-model']")
    CLICK_SEO = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(11) > a")
    INPUT_SEO = (By.CSS_SELECTOR, "input[id='input-keyword-0-1']")
    CHECK_BOX = (By.CSS_SELECTOR, "input[name='agree']")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    ACCEPT = (By.CSS_SELECTOR, "#content > div > a")
    LOGOUT_BTN = (By.CSS_SELECTOR, "#nav-logout > a > span")
    DEL_PROD_CHECK = (By.CSS_SELECTOR, "#form-product > div.table-responsive > table > tbody > tr:nth-child(3) > td:nth-child(1) > input")
    DEl_PROD_BTN = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger")

    ADMIN_NAME = "user"
    PASSWD = "bitnami"
    SECOND_NAME = f"myPROD-{random_string()}"

    def input_admin_credentials(self):
        self.input_value(self.INPUT_NAME, self.ADMIN_NAME)
        self.input_value(self.INPUT_PASSWD, self.PASSWD)

    def click_catalog(self):
        self.click(self.CATALOG)

    def click_products(self):
        self.click(self.PRODUCTS)

    def navigate_to_products(self):
        self.click_catalog()
        self.click_products()

    def add_prod(self):
        self.click(self.ADD_PRODUCT)

    def click_descr(self):
        self.click(self.CLICL_CAT)

    def input_category(self):
        self.input_value(self.INPUT_CATEGORY, self.SECOND_NAME)

    def input_tagy(self):
        self.input_value(self.INPUT_TAG, self.SECOND_NAME)

    def click_seo(self):
        self.click(self.CLICK_SEO)

    def input_seo(self):
        self.input_value(self.INPUT_SEO, self.SECOND_NAME)

    def click_data(self):
        self.click(self.CLICK_DATA)

    def input_model(self):
        self.input_value(self.INPUT_MODEl, self.SECOND_NAME)

    def submit(self):
        self.click(self.SUBMIT)

    def accept_alert(self):
        self.browser.switch_to.alert.accept()

    def delete_product(self):
        self.click(self.DEL_PROD_CHECK)
        self.click(self.DEl_PROD_BTN)
        self.accept_alert()

    def select_product_checkbox_by_name(self, product_name):
        """
        Selects the checkbox of a product by its name in the products list.
        """
        product_row_xpath = f"//td[contains(text(), '{product_name}')]/preceding-sibling::td/input[@type='checkbox']"
        checkbox = self.get_element((By.XPATH, product_row_xpath))
        checkbox.click()