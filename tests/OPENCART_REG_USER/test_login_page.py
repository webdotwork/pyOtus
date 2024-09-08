import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.main_page import MainPage
from page_objects.register_user_page import RegisterUser
import logging
import time

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def take_screenshot(browser, name):
    allure.attach(browser.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

@pytest.mark.usefixtures("browser")
def test_navigate_to_login(browser):
    logger.info('====== Started: {} ======'.format(int(time.time())))
    try:
        with allure.step('Navigating to Main Page and clicking My Account'):
            main_page = MainPage(browser)
            main_page.click_my_account()
            take_screenshot(browser, 'Main Page - My Account')

        with allure.step('Clicking Login'):
            main_page.click_login()
            take_screenshot(browser, 'Main Page - Login')

        with allure.step('Checking Login Form Presence'):
            login_input = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input"))
            )
            assert login_input, "Login input field not found. Navigation to login page failed."
            take_screenshot(browser, 'Login Page')

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        take_screenshot(browser, 'Error')
        raise

@pytest.mark.parametrize("last_name, email, password", [
    ("Doe", "john.doe@example.com", "password123"),
    ("Smith", "jane.smith@example.com", "securePass!"),
    ("Johnson", "bob.johnson@example.com", "password456")
])
@pytest.mark.usefixtures("browser")
def test_registration_missing_first_name(browser, last_name, email, password):
    logger.info('====== Started: {} ======'.format(int(time.time())))
    try:
        with allure.step('Navigating to Main Page and clicking My Account'):
            logger.debug('Navigating to Main Page')
            main_page = MainPage(browser)
            logger.debug('Clicking My Account')
            main_page.click_my_account()
            take_screenshot(browser, 'Main Page - My Account')

        with allure.step('Clicking Register User'):
            logger.debug('Clicking Register User')
            main_page.click_register_user()
            take_screenshot(browser, 'Main Page - Register User')

        with allure.step('Filling registration form with missing first name'):
            logger.debug('Filling registration form with missing first name')
            register_user = RegisterUser(browser)
            register_user.input_data(register_user.INPUT_FIRST_NAME, "")
            register_user.input_data(register_user.INPUT_SECOND_NAME, last_name)
            register_user.input_data(register_user.INPUT_EMAIL, email)
            register_user.input_data(register_user.INPUT_PASSWD, password)
            take_screenshot(browser, 'Registration Form with Missing First Name')

        with allure.step('Agreeing to terms and conditions'):
            logger.debug('Agreeing to terms and conditions')
            register_user.click_check_box()
            take_screenshot(browser, 'Agreed to Terms and Conditions')

        with allure.step('Submitting registration form'):
            logger.debug('Submitting registration form')
            register_user.submit()
            take_screenshot(browser, 'Registration Form Submitted')

        with allure.step('Checking for error'):
            logger.debug('Checking for error')
            assert "error" in browser.page_source, "No error message for missing first name."
            take_screenshot(browser, 'Error Message for Missing First Name')

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        take_screenshot(browser, 'Error')
        raise