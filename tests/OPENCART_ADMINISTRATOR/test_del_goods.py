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


@pytest.mark.usefixtures("browser")
def test_delete_specific_product(browser):
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

        product_name = "myPROD-"  # Replace with an actual product
        logger.debug(f'Selecting product "{product_name}" for deletion')
        if admin_page.select_product_checkbox_by_name(product_name):
            admin_page.delete_product()
            logger.info(f'Product "{product_name}" was deleted successfully')
        else:
            logger.warning(f'Product "{product_name}" not found for deletion')

        logger.debug('Verifying if the product is still present')
        admin_page.navigate_to_products()
        if not admin_page.select_product_checkbox_by_name(product_name):
            logger.info(f'Product "{product_name}" successfully deleted from the list')
        else:
            logger.warning(f'Product "{product_name}" still exists in the product list')

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        raise
