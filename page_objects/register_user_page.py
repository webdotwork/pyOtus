from selenium.webdriver.common.by import By
from helpers import random_string, random_email
from page_objects.base_page import BasePage


class RegisterUser(BasePage):
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "input[id='input-firstname']")
    INPUT_SECOND_NAME = (By.CSS_SELECTOR, "input[id='input-lastname']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[id='input-email']")
    INPUT_PASSWD = (By.CSS_SELECTOR, "input[id='input-password']")
    CHECK_BOX = (By.CSS_SELECTOR, "input[name='agree']")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    ACCEPT = (By.CSS_SELECTOR, "#content > div > a")
    LOGOUT_BTN = (By.CSS_SELECTOR, "#column-right > div > a:nth-child(13)")

    FIRST_NAME = random_string()
    SECOND_NAME = random_string()
    EMAIL = random_email()
    PASSWD = random_string()

    def input_data(self, locator, value):
        self.input_value(locator, value)

    def fill_registration_form(self):
        data = [
            (self.INPUT_FIRST_NAME, self.FIRST_NAME),
            (self.INPUT_SECOND_NAME, self.SECOND_NAME),
            (self.INPUT_EMAIL, self.EMAIL),
            (self.INPUT_PASSWD, self.PASSWD)
        ]
        for locator, value in data:
            self.input_data(locator, value)

    def click_check_box(self):
        self.click(self.CHECK_BOX)

    def submit(self):
        self.click(self.SUBMIT)

    def accept(self):
        self.click(self.ACCEPT)

    def logout(self):
        self.click(self.LOGOUT_BTN)

# from selenium.webdriver.common.by import By
# from helpers import random_string
# from page_objects.base_page import BasePage
# from helpers import random_email
#
# class RegisterUser(BasePage):
#
#     INPUT_FIRST_NAME = By.CSS_SELECTOR, "input[id='input-firstname']"
#     INPUT_SECOND_NAME = By.CSS_SELECTOR, "input[id='input-lastname']"
#     INPUT_EMAIL = By.CSS_SELECTOR, "input[id='input-email']"
#     INPUT_PASSWD = By.CSS_SELECTOR, "input[id='input-password']"
#     CHECK_BOX = By.CSS_SELECTOR, "input[name='agree']"
#     SUBMIT = By.CSS_SELECTOR, "button[type='submit']"
#     ACCEPT = By.CSS_SELECTOR, "#content > div > a"
#     LOGOUT_BTN = By.CSS_SELECTOR, "#column-right > div > a:nth-child(13)"
#     FIRST_NAME = random_string()
#     SECOND_NAME = random_string()
#     EMAIL = random_email()
#     PASSWD = random_email()
#     SBM = By.CSS_SELECTOR, "#form-login > div.text-end > button"
#     # EMAIL_N = "testuser123@hmil.com"
#     # PASSWD_N = "Testuser@123"
#
#     def get_inputs(self):
#         return self.get_elements(self.INPUT_FIRST_NAME)
#
#     def input_data_first_name(self):
#         self.input_value(self.INPUT_FIRST_NAME, self.FIRST_NAME)
#
#     def input_data_second_name(self):
#         self.input_value(self.INPUT_SECOND_NAME, self.SECOND_NAME)
#
#     def input_data_email(self):
#         self.input_value(self.INPUT_EMAIL, self.EMAIL)
#
#
#     def input_data_passwd(self):
#         self.input_value(self.INPUT_PASSWD, self.PASSWD)
#
#
#     # def input_data_email_n(self):
#     #     text =
#     #     self.input_value(self.INPUT_PASSWD, text)
#
#     # def input_data_passwd_n(self, text):
#     #     self.input_value(self.INPUT_EMAIL, text)
#     def click_check_box(self):
#         self.click(self.CHECK_BOX)
#     def submit(self):
#         self.click(self.SUBMIT)
#
#     def sbm(self):
#         self.click(self.SBM)
#
#     def accept(self):
#         self.click(self.SUBMIT)
#
#     def logout(self):
#         self.click(self.LOGOUT_BTN)
#
