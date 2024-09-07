import pytest
from pyOtus.page_objects.admin_page import AdminPage
import logging
import time

# Configure logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

@pytest.mark.usefixtures("browser")
def test_del_prod(browser):
    logger.info('====== Started: {} ======'.format(int(time.time())))
    try:
        logger.debug('Opening Admin Page')
        admin_page = AdminPage(browser)

        logger.debug('Inputting admin credentials')
        admin_page.input_admin_credentials()

        logger.debug('Submitting admin credentials')
        admin_page.submit()

        logger.debug('Navigating to Catalog and Products')
        admin_page.navigate_to_products()

        logger.debug('Selecting product checkbox for deletion and confirming')
        admin_page.delete_product()

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        raise


# import pytest
# import time
# from page_objects.admin_page import AdminPage
# import logging
#
# # Configure logging
# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('example.log')
# file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# logger.addHandler(file_handler)
# logger.setLevel(logging.DEBUG)
#
# @pytest.mark.usefixtures("browser")
# def test_del_prod(browser):
#     logger.info('====== Started: {} ======'.format(int(time.time())))
#     try:
#         logger.debug('Opening Admin Page')
#         admin_page = AdminPage(browser)
#
#         logger.debug('Inputting admin credentials')
#         admin_page.input_admin_credentials()
#
#         logger.debug('Submitting admin credentials')
#         admin_page.submit()
#
#         logger.debug('Navigating to Catalog and Products')
#         admin_page.navigate_to_products()
#
#         logger.debug('Selecting product checkbox for deletion')
#         admin_page.delete_product()
#
#         logger.info('====== Finished: {} ======'.format(int(time.time())))
#
#     except Exception as e:
#         logger.error('Error during test execution: %s', e)
#         raise
#
#
#
#
# # import pytest
# # import time
# # from page_objects.admin_page import AdminPage
# # import logging
# #
# # # Configure logging
# # logger = logging.getLogger(__name__)
# # file_handler = logging.FileHandler('example.log')
# # file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# # logger.addHandler(file_handler)
# # logger.setLevel(logging.DEBUG)
# #
# #
# # @pytest.mark.usefixtures("browser")
# # def test_del_prod(browser):
# #     logger.info('====== Started: {} ======'.format(int(time.time())))
# #     try:
# #         logger.debug('Opening Admin Page')
# #         admin_page = AdminPage(browser)
# #
# #         logger.debug('Inputting admin name')
# #         admin_page.input_admin_name()
# #
# #         logger.debug('Inputting admin password')
# #         admin_page.input_data_passwd()
# #
# #         logger.debug('Submitting admin credentials')
# #         admin_page.submit()
# #
# #         logger.debug('Navigating to Catalog')
# #         admin_page.click_catalog()
# #
# #         logger.debug('Navigating to Products')
# #         admin_page.click_products()
# #
# #         logger.debug('Selecting product checkbox for deletion')
# #         admin_page.click_check_box_prod()
# #
# #         logger.debug('Clicking delete product')
# #         admin_page.click_del_prod()
# #
# #         logger.debug('Accepting alert to confirm deletion')
# #         admin_page.accept_alert()
# #
# #         logger.info('====== Finished: {} ======'.format(int(time.time())))
# #
# #     except Exception as e:
# #         logger.error('Error during test execution: %s', e)
# #         raise
