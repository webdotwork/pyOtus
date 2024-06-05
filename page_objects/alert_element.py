from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccessElement:
    SUCCESS_ALERT = By.CSS_SELECTOR, ".alert-success"
    LOGIN_LINK = By.LINK_TEXT, "login"
    SHOPPING_CART_LINK = By.LINK_TEXT, "shopping cart"
    COMPARISON_LINK = By.LINK_TEXT, "product comparison"

    def __init__(self, browser):
        self.browser = browser
        self.alert = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT))

    @property
    def login(self):
        return self.alert.find_element(*self.LOGIN_LINK)

    @property
    def shopping_cart(self):
        return self.alert.find_element(*self.SHOPPING_CART_LINK)

    @property
    def comparison(self):
        return self.alert.find_element(*self.COMPARISON_LINK)
