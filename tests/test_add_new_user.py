import pytest
from page_objects.register_user_page import RegisterUser
from page_objects.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# Configure logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


@pytest.mark.usefixtures("browser")
def test_add_new_user(browser):
    logger.info('====== Started: {} ======'.format(int(time.time())))
    try:
        logger.debug('Navigating to Main Page')
        main_page = MainPage(browser)

        logger.debug('Clicking My Account')
        main_page.click((By.CSS_SELECTOR, "a[title='My Account']"))

        logger.debug('Clicking Register User')
        main_page.click((By.CSS_SELECTOR, "a[title='Register']"))

        logger.debug('Filling registration form')
        register_user = RegisterUser(browser)
        register_user.fill_registration_form()

        logger.debug('Agreeing to terms and conditions')
        register_user.agree_to_terms()

        logger.debug('Submitting registration form')
        register_user.submit_registration()

        logger.debug('Accepting registration')
        register_user.accept_registration()

        logger.debug('Logging out new user')
        register_user.logout()

        logger.debug('Checking if "My Account" link is present')
        check = WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#column-right > div > a:nth-child(4)")))
        assert check.text == 'My Account', "тест провален DUDE!!"

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        raise
