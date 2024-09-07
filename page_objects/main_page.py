from selenium.webdriver.common.by import By

from pyOtus.page_objects.base_page import BasePage


class MainPage(BasePage):
    FEATURED_PRODUCT_NAME = By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a"
    MY_ACC = By.CSS_SELECTOR, "#top > div > div.nav.float-end > ul > li:nth-child(2)"  #"#top > div > div.nav.float-end > ul > li" #"#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a"
    REGISTER_USER = By.CSS_SELECTOR, "#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a"
    LOGIN_USER = By.CSS_SELECTOR, "#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(2) > a"
    def get_featured_product_name(self, index=0):
        return self.get_elements(self.FEATURED_PRODUCT_NAME)[index].text

    def click_featured_product(self, index=0):
        if index == 0:
            self.click(self.FEATURED_PRODUCT_NAME)
        else:
            self.get_elements(self.FEATURED_PRODUCT_NAME)[index].click()


    # def get_my_account(self, index=0):
    #     return self.get_elements(self.MY_ACC)[index].text

    def click_my_account(self, index=0):
        if index == 0:
            self.click(self.MY_ACC)
        else:
            self.get_elements(self.MY_ACC)[index].click()

    def click_login(self, index=0):
        if index == 0:
            self.click(self.LOGIN_USER)
        else:
            self.get_elements(self.LOGIN_USER)[index].click()


    def click_register_user(self, index=0):
        if index == 0:
            self.click(self.REGISTER_USER)
        else:
            self.get_elements(self.REGISTER_USER)[index].click()