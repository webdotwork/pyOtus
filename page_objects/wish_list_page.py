from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class WishListPage(BasePage):
    WISH_LIST = By.XPATH, "//*[@id='account-wishlist']"

    def _product_name(self, product_name):
        return By.XPATH, self.WISH_LIST[1] + self._text_xpath(product_name)

    def wait_for_product_in_wish_list(self, product_name):
        self.get_element(self._product_name(product_name))
