from page_objects.register_user_page import RegisterUser
from page_objects.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_new_user(browser):
    MainPage(browser).click_my_account()
    MainPage(browser).click_register_user()
    RegisterUser(browser).input_data_first_name()
    RegisterUser(browser).input_data_second_name()
    RegisterUser(browser).input_data_email()
    RegisterUser(browser).input_data_passwd()
    RegisterUser(browser).click_check_box()
    RegisterUser(browser).submit()
    RegisterUser(browser).accept()
    RegisterUser(browser).logout()
    check = WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#column-right > div > a:nth-child(4)")))
    assert check.text == 'My Account', "тест провален DUDE!!"