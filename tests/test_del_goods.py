import time
from page_objects.admin_page import AdminPage

def test_del_prod(browser):
    AdminPage(browser).input_admin_name()
    AdminPage(browser).input_data_passwd()
    AdminPage(browser).submit()
    AdminPage(browser).click_catalog()
    AdminPage(browser).click_products()
    AdminPage(browser).click_check_box_prod()
    AdminPage(browser).click_del_prod()
    AdminPage(browser).accept_alert()