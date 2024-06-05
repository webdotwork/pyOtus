from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _text_xpath(self, text):
        return f"//*[text()='{text}']"


    def get_element(self, locator: Tuple[str, str], timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: Tuple[str, str], timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: Tuple[str, str]):
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.3).click().perform()


    def input_value(self, locator: Tuple[str, str], text: str):
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)
