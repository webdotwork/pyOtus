import pytest
from pyOtus.page_objects.register_user_page import RegisterUser
from pyOtus.page_objects.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time


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
        main_page.click((By.CSS_SELECTOR, "#top > div > div.nav.float-end > ul > li:nth-child(2) > div > a"))

        logger.debug('Clicking Register User')
        main_page.click((By.CSS_SELECTOR, "#top > div > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a"))

        logger.debug('Filling registration form')
        register_user = RegisterUser(browser)
        register_user.fill_registration_form()

        logger.debug('Agreeing to terms and conditions')
        register_user.click_check_box()

        logger.debug('Submitting registration form')
        register_user.submit()

        logger.debug('Accepting registration')
        register_user.accept()

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
