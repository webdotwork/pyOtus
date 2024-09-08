import pytest
import random
import time
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import logging

# Configure logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


@pytest.mark.usefixtures("browser")
def test_main_page_currency(browser):
    logger.info('====== Started: {} ======'.format(int(time.time())))
    try:
        logger.debug('Getting list of currency switch options')
        base_page = BasePage(browser)
        currency_switch_list = base_page.get_elements((By.CSS_SELECTOR, "#form-currency > div > a"))

        logger.debug('Clicking on the first currency switch option')
        currency_switch_list[0].click()

        random_currency_selector = f"#form-currency > div > ul > li:nth-child({random.randint(1, 3)}) > a"
        logger.debug(f'Randomly selecting a currency with selector: {random_currency_selector}')
        random_what_ever = base_page.get_element((By.CSS_SELECTOR, random_currency_selector))

        logger.debug('Clicking the randomly selected currency option')
        random_what_ever.click()

        logger.debug('Getting current currency symbol')
        current_currency = base_page.get_element((By.CSS_SELECTOR, "#form-currency > div > a > strong"))

        logger.debug('Getting list of new prices to check currency')
        currency_check = base_page.get_elements((By.CSS_SELECTOR, ".price-new"))

        for c in currency_check:
            try:
                currency = c.text
                assert current_currency.text in currency, "Current currency not found in price"
                logger.debug(f'Current currency: {current_currency.text}, Price checked: {currency}')
            except Exception as e:
                logger.error(f'Error checking currency in price: {e}')
                raise

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        raise
    finally:
        time.sleep(1)  # Pause for demonstration

