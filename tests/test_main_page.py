import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page_element(browser):
    browser.get(browser.url)
    browser.find_element(By.ID, "alert")
    browser.find_element(By.NAME, "search")
    browser.find_element(By.CSS_SELECTOR, "button[type='button']")
    browser.find_element(By.LINK_TEXT, "MacBook")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")

def test_main_page_menu(browser):
    menu_items = browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")
    assert len(menu_items) == 8, "Неверное количество элементов меню"


def test_main_page_fetured_items(browser):
    fetured_items = browser.find_elements(By.CLASS_NAME, "product-thumb")
    assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"


def test_main_page_footer_blocks(browser):
    footer_blocks = browser.find_elements(By.XPATH, "//footer//ul")
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"


def test_main_page_open_product(browser):
    fetured_items = browser.find_elements(By.CLASS_NAME, "product-thumb")
    fetured_items[2].click()
    browser.find_element(By.LINK_TEXT, "Specification")

def test_main_page_curency(browser):
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
    time.sleep(1)  # Пауза для демонстрации