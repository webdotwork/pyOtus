from selenium.webdriver.common.by import By
from pyOtus.helpers import random_string, random_email
from pyOtus.page_objects.base_page import BasePage

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
    LOGOUT_BTN = (By.CSS_SELECTOR, "#column-right > div > a:nth-child(13)")
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



# from selenium.webdriver.common.by import By
# from page_objects.base_page import BasePage
# from helpers import random_string, random_email
#
# class AdminPage(BasePage):
#
#     INPUT_NAME = (By.CSS_SELECTOR, "input[name='username']")
#     INPUT_PASSWD = (By.CSS_SELECTOR, "input[name='password']")
#     SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
#     CATALOG = (By.CSS_SELECTOR, "#menu-catalog > a")
#     PRODUCTS = (By.CSS_SELECTOR, "#collapse-1 > li:nth-child(2) > a")
#     ADD_PRODUCT = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a")
#     CLICK_CAT = (By.CSS_SELECTOR, "#language-1 > div:nth-child(1) > div")
#     INPUT_CATEGORY = (By.CSS_SELECTOR, "#input-name-1")
#     INPUT_TAG = (By.CSS_SELECTOR, "input[id='input-meta-title-1']")
#     CLICK_DATA = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a")
#     INPUT_MODEL = (By.CSS_SELECTOR, "input[id='input-model']")
#     CLICK_SEO = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(11) > a")
#     INPUT_SEO = (By.CSS_SELECTOR, "input[id='input-keyword-0-1']")
#     DEL_PROD_CHECK = (By.CSS_SELECTOR, "#form-product > div.table-responsive > table > tbody > tr:nth-child(3) > td:nth-child(1) > input")
#     DEL_PROD_BTN = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger")
#     LOGOUT_BTN = (By.CSS_SELECTOR, "#column-right > div > a:nth-child(13)")
#
#     ADMIN_NAME = "user"
#     PASSWD = "bitnami"
#     SECOND_NAME = f"myPROD-{random_string()}"
#
#     def input_admin_credentials(self):
#         self.input_value(self.INPUT_NAME, self.ADMIN_NAME)
#         self.input_value(self.INPUT_PASSWD, self.PASSWD)
#
#     def navigate_to_products(self):
#         self.click(self.CATALOG)
#         self.click(self.PRODUCTS)
#
#     def add_product(self):
#         self.click(self.ADD_PRODUCT)
#         self.click(self.CLICK_CAT)
#         self.input_value(self.INPUT_CATEGORY, self.SECOND_NAME)
#         self.input_value(self.INPUT_TAG, self.SECOND_NAME)
#         self.click(self.CLICK_DATA)
#         self.input_value(self.INPUT_MODEL, self.SECOND_NAME)
#         self.click(self.CLICK_SEO)
#         self.input_value(self.INPUT_SEO, self.SECOND_NAME)
#         self.click(self.SUBMIT)
#
#     def delete_product(self):
#         self.click(self.DEL_PROD_CHECK)
#         self.click(self.DEL_PROD_BTN)
#         self.accept_alert()
#
#     def logout(self):
#         self.click(self.LOGOUT_BTN)
#
#     def accept_alert(self):
#         self.browser.switch_to.alert.accept()




# from random import choice
# from selenium.webdriver.common.by import By
# from helpers import random_string
# from page_objects.base_page import BasePage
# from helpers import random_email
# from helpers import random_phone
# class AdminPage(BasePage):
#
#     INPUT_NAME = By.CSS_SELECTOR, "input[name='username']"
#     CATALOG = By.CSS_SELECTOR, "#menu-catalog > a"
#     PRODUCTS = By.CSS_SELECTOR, "#collapse-1 > li:nth-child(2) > a"
#     ADD_PRODUCT = By.CSS_SELECTOR, "#content > div.page-header > div > div > a"
#     CLICL_CAT = By.CSS_SELECTOR, "#language-1 > div:nth-child(1) > div"
#     INPUT_CATEGORY = By.CSS_SELECTOR, "#input-name-1" #"input[id='input-name-1]']"
#     INPUT_TAG = By.CSS_SELECTOR, "input[id='input-meta-title-1']"
#     CLICK_DATA = By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2) > a"
#     INPUT_MODEl = By.CSS_SELECTOR, "input[id='input-model']"
#     CLICK_SEO = By.CSS_SELECTOR, "#form-product > ul > li:nth-child(11) > a"
#     INPUT_SEO = By.CSS_SELECTOR, "input[id='input-keyword-0-1']"
#     INPUT_PASSWD = By.CSS_SELECTOR, "input[name='password']"
#     CHECK_BOX = By.CSS_SELECTOR, "input[name='agree']"
#     SUBMIT = By.CSS_SELECTOR, "button[type='submit']"
#     ACCEPT = By.CSS_SELECTOR, "#content > div > a"
#     LOGOUT_BTN = By.CSS_SELECTOR, "#column-right > div > a:nth-child(13)"
#     ADMIN_NAME = "user"
#     SECOND_NAME = f"myPROD-{random_string()}"
#     EMAIL = random_email()
#     PASSWD = "bitnami"
#     DEL_PROD_CHECK = By.CSS_SELECTOR, "#form-product > div.table-responsive > table > tbody > tr:nth-child(3) > td:nth-child(1) > input"
#     DEl_PROD_BTN = By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger"
#
#     # def get_products(self):
#     #     p_list = self.get_elements(self.GET_PRODUCT_LIST)
#     #     for p in choices(p_list, k=1):
#     #         return  self.click(p)
#
#     def get_inputs(self):
#         return self.get_elements(self.INPUT_FIRST_NAME)
#
#     def input_admin_name(self):
#         self.input_value(self.INPUT_NAME, self.ADMIN_NAME)
#
#     def click_catalog(self):
#         self.click(self.CATALOG)
#
#     def click_products(self):
#         self.click(self.PRODUCTS)
#
#     def click_descr(self):
#         self.click(self.CLICL_CAT)
#
#     def add_prod(self):
#         self.click(self.ADD_PRODUCT)
#     def input_category(self):
#         self.input_value(self.INPUT_CATEGORY, self.SECOND_NAME)
#
#     def input_tagy(self):
#         self.input_value(self.INPUT_TAG, self.SECOND_NAME)
#
#
#     def input_seo(self):
#         self.input_value(self.INPUT_SEO, self.SECOND_NAME)
#     def input_model(self):
#         self.input_value(self.INPUT_MODEl, self.SECOND_NAME)
#
#     def click_seo(self):
#         self.click(self.CLICK_SEO)
#     def click_data(self):
#         self.click(self.CLICK_DATA)
#     # def input_data_email(self):
#     #     self.input_value(self.INPUT_EMAIL, self.EMAIL)
#
#     def input_data_passwd(self):
#         self.input_value(self.INPUT_PASSWD, self.PASSWD)
#
#     def click_check_box(self):
#         self.click(self.CHECK_BOX)
#     def click_check_box_prod(self):
#         self.click(self.DEL_PROD_CHECK)
#     def click_del_prod(self):
#         self.click(self.DEl_PROD_BTN)
#     def submit(self):
#         self.click(self.SUBMIT)
#
#     def accept(self):
#         self.click(self.SUBMIT)
#
#     def logout(self):
#         self.click(self.LOGOUT_BTN)
#
#     def accept_alert(self):
#         self.browser.switch_to.alert.accept()
