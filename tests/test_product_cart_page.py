import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages import LoginAdminPage

#
def test_login_page_external(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)


def test_main_page_curency(browser):
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "product-thumb")))
    fetured_items = browser.find_elements(By.CLASS_NAME, "product-thumb")
    fetured_items[2].click()
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "dropdown-toggle")))
    curency_switch = browser.find_elements(By.CLASS_NAME, "dropdown-toggle")
    curency_switch[0].click()
    browser.find_element(By.CSS_SELECTOR, f"#form-currency > div > ul > li:nth-child({random.randint(1, 3)}) > a").click()
    curent_curency = browser.find_element(By.CSS_SELECTOR, "#form-currency > div > a > strong") # Пауза для демонстрации
    curency_check = browser.find_elements(By.CLASS_NAME, "price-new")
    for c in curency_check:
        try:
            curency = c.text
            assert curent_curency.text in curency
            print(f'curent curency: {curent_curency.text}\ncurency_check: {curency}')
        except Exception as e:
            print("Error:", e)
