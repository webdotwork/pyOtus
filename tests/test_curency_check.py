import random
import time
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
def test_main_page_curency(browser):
    curency_switch_list = BasePage(browser).get_elements((By.CSS_SELECTOR, "#form-currency > div > a"))
    curency_switch_list[0].click()
    random_what_ever = BasePage(browser).get_element((By.CSS_SELECTOR, f"#form-currency > div > ul > li:nth-child({random.randint(1, 3)}) > a"))
    random_what_ever.click()
    curent_curency = BasePage(browser).get_element((By.CSS_SELECTOR, "#form-currency > div > a > strong")) # Пауза для демонстрации
    curency_check = BasePage(browser).get_elements((By.CSS_SELECTOR, ".price-new"))
    for c in curency_check:
        try:
            curency = c.text
            assert curent_curency.text in curency
            print(f'curent curency: {curent_curency.text}\ncurency_check: {curency}')
        except Exception as e:
            print("Error:", e)
    time.sleep(1)  # Пауза для демонстрации