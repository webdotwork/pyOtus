import pytest
from page_objects.admin_page import AdminPage
import logging
import time

# Configure logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

@pytest.mark.usefixtures("browser")
def test_add_new_goods(browser):
    logger.info('====== Started: {} ======'.format(int(time.time())))
    try:
        logger.debug('Opening Admin Page')
        admin_page = AdminPage(browser)

        logger.debug('Inputting admin credentials')
        admin_page.input_admin_credentials()

        logger.debug('Submitting admin credentials')
        admin_page.submit()

        logger.debug('Navigating to Catalog')
        admin_page.click_catalog()

        logger.debug('Navigating to Products')
        admin_page.click_products()

        logger.debug('Adding new product')
        admin_page.add_prod()

        logger.debug('Entering product description')
        admin_page.click_descr()

        logger.debug('Entering product category')
        admin_page.input_category()

        logger.debug('Entering product tags')
        admin_page.input_tagy()

        logger.debug('Navigating to SEO tab')
        admin_page.click_seo()

        logger.debug('Entering SEO data')
        admin_page.input_seo()

        logger.debug('Navigating to Data tab')
        admin_page.click_data()

        logger.debug('Entering product model')
        admin_page.input_model()

        logger.debug('Submitting new product form')
        admin_page.submit()

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        raise



# import pytest
# from page_objects.admin_page import AdminPage
# import logging
# import time
#
# # Configure logging
# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('example.log')
# file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)
#
#
# @pytest.mark.usefixtures("browser")
# def test_add_new_goods(browser):
#     logger.info('====== Started: {} ======'.format(int(time.time())))
#     try:
#         logger.debug('Opening Admin Page')
#         admin_page = AdminPage(browser)
#
#         logger.debug('Inputting admin name')
#         admin_page.input_admin_name()
#
#         logger.debug('Inputting admin password')
#         admin_page.input_data_passwd()
#
#         logger.debug('Submitting admin credentials')
#         admin_page.submit()
#
#         logger.debug('Navigating to Catalog')
#         admin_page.click_catalog()
#
#         logger.debug('Navigating to Products')
#         admin_page.click_products()
#
#         logger.debug('Adding new product')
#         admin_page.add_prod()
#
#         logger.debug('Entering product description')
#         admin_page.click_descr()
#
#         logger.debug('Entering product category')
#         admin_page.input_category()
#
#         logger.debug('Entering product tags')
#         admin_page.input_tagy()
#
#         logger.debug('Navigating to SEO tab')
#         admin_page.click_seo()
#
#         logger.debug('Entering SEO data')
#         admin_page.input_seo()
#
#         logger.debug('Navigating to Data tab')
#         admin_page.click_data()
#
#         logger.debug('Entering product model')
#         admin_page.input_model()
#
#         logger.debug('Submitting new product form')
#         admin_page.submit()
#
#         logger.info('====== Finished: {} ======'.format(int(time.time())))
#
#     except Exception as e:
#         logger.error('Error during test execution: %s', e)
#         raise
