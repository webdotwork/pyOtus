from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_main_page_curency(browser):
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2) > div > div.content > form > div > button:nth-child(1)")))
    form = browser.find_element(By.CSS_SELECTOR, "form:nth-child(2)")
    buttons = form.find_elements(By.TAG_NAME, "button")
    buttons[0].click()
    element = browser.find_element(By.CSS_SELECTOR, "#header-cart > div > button")
    assert element.text != "Your shopping cart is empty!"