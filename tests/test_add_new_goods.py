from page_objects.admin_page import AdminPage

def test_add_new_goods(browser):
    AdminPage(browser).input_admin_name()
    AdminPage(browser).input_data_passwd()
    AdminPage(browser).submit()
    AdminPage(browser).click_catalog()
    AdminPage(browser).click_products()
    AdminPage(browser).add_prod()
    AdminPage(browser).click_descr()
    AdminPage(browser).input_category()
    AdminPage(browser).input_tagy()
    AdminPage(browser).click_seo()
    AdminPage(browser).input_seo()
    AdminPage(browser).click_data()
    AdminPage(browser).input_model()
    AdminPage(browser).submit()
    # time.sleep(30)