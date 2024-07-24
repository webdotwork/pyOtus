import time

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class UserPage(BasePage):
    LOGIN_INPUT = By.CSS_SELECTOR, "#input-username"
    PASSWORD_INPUT = By.CSS_SELECTOR, "#input-password"
    SUBMIT_LOGIN_BUTTON = By.CSS_SELECTOR, "#form-login button"
    LOGOUT_LINK = By.LINK_TEXT, "Logout"
    USER_MENU = By.XPATH, "//*[@id='column-right']"
    WISH_LIST_LINK = By.XPATH, USER_MENU[1] + "//*[text()='Wish List']"


    # def log(self, username, password):
    #     self.get_element(loca)

    def login(self, username, password):
        self.input_value(self.LOGIN_INPUT, username)
        self.input_value(self.PASSWORD_INPUT, password)
        # self.click(self.SUBMIT_LOGIN_BUTTON)
        time.sleep(5)
        return self

    def wait_logged_in(self):
        self.get_element(self.LOGOUT_LINK)
        return self

    def click_wish_list(self):
        self.click(self.WISH_LIST_LINK)
