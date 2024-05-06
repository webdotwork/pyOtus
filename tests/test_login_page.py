from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from pages import LoginAdminPage


def test_login_page_external(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)

@pytest.mark.parametrize(["path", "username", "password"], [("/administration", "user", "bitnami")])
def test_login_page_menu(browser, path, username, password):
    browser.get(browser.url + path)
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    name = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nav-profile > a > span")))
    assert name.text == '   John Doe', "Неверное количество элементов меню"
    browser.find_element(By.CSS_SELECTOR, "#nav-logout > a > span").click()


def test_login_page_fetured_items(browser):
    fetured_items = browser.find_elements(By.CLASS_NAME, "product-thumb")
    assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"
