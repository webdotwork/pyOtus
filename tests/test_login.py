import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.main_page import MainPage
from page_objects.register_user_page import RegisterUser
import logging
import time

# Configure logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levellevel)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def take_screenshot(browser, name):
    allure.attach(browser.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

@pytest.mark.usefixtures("browser")
def test_login(browser):
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

        with allure.step('Filling registration form'):
            logger.debug('Filling registration form')
            register_user = RegisterUser(browser)
            register_user.fill_registration_form()
            take_screenshot(browser, 'Registration Form Filled')

        with allure.step('Agreeing to terms and conditions'):
            logger.debug('Agreeing to terms and conditions')
            register_user.click_check_box()
            take_screenshot(browser, 'Agreed to Terms and Conditions')

        with allure.step('Submitting registration form'):
            logger.debug('Submitting registration form')
            register_user.submit()
            take_screenshot(browser, 'Registration Form Submitted')

        with allure.step('Accepting registration'):
            logger.debug('Accepting registration')
            register_user.accept()
            take_screenshot(browser, 'Registration Accepted')

        with allure.step('Logging out new user'):
            logger.debug('Logging out new user')
            register_user.logout()
            take_screenshot(browser, 'User Logged Out')

        with allure.step('Navigating back to My Account and clicking Login'):
            logger.debug('Navigating back to My Account')
            main_page.click_my_account()
            logger.debug('Clicking Login')
            main_page.click_login()
            take_screenshot(browser, 'Main Page - Login')

        with allure.step('Entering login credentials and submitting'):
            logger.debug('Entering login credentials')
            register_user.input_data(RegisterUser.INPUT_EMAIL, RegisterUser.EMAIL)
            register_user.input_data(RegisterUser.INPUT_PASSWD, RegisterUser.PASSWD)
            logger.debug('Submitting login form')
            browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            take_screenshot(browser, 'Login Form Submitted')

        with allure.step('Checking if "My Account" link is present'):
            logger.debug('Checking if "My Account" link is present')
            check = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#column-right > div > a:nth-child(4)")))
            assert check.text == 'My Account', "тест провален DUDE!!"
            take_screenshot(browser, 'My Account Link Present')

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        take_screenshot(browser, 'Error')
        raise



# import pytest


# import allure
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from page_objects.main_page import MainPage
# from page_objects.register_user_page import RegisterUser
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
# def take_screenshot(browser, name):
#     allure.attach(browser.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)
#
#
# @pytest.mark.usefixtures("browser")
# def test_login(browser):
#     logger.info('====== Started: {} ======'.format(int(time.time())))
#     try:
#         with allure.step('Navigating to Main Page and clicking My Account'):
#             logger.debug('Navigating to Main Page')
#             main_page = MainPage(browser)
#             logger.debug('Clicking My Account')
#             main_page.click_my_account()
#             take_screenshot(browser, 'Main Page - My Account')
#
#         with allure.step('Clicking Register User'):
#             logger.debug('Clicking Register User')
#             main_page.click_register_user()
#             take_screenshot(browser, 'Main Page - Register User')
#
#         with allure.step('Filling registration form'):
#             logger.debug('Filling registration form')
#             register_user = RegisterUser(browser)
#             register_user.input_data_first_name()
#             register_user.input_data_second_name()
#             register_user.input_data_email()
#             register_user.input_data_passwd()
#             take_screenshot(browser, 'Registration Form Filled')
#
#         with allure.step('Agreeing to terms and conditions'):
#             logger.debug('Agreeing to terms and conditions')
#             register_user.click_check_box()
#             take_screenshot(browser, 'Agreed to Terms and Conditions')
#
#         with allure.step('Submitting registration form'):
#             logger.debug('Submitting registration form')
#             register_user.submit()
#             take_screenshot(browser, 'Registration Form Submitted')
#
#         with allure.step('Accepting registration'):
#             logger.debug('Accepting registration')
#             register_user.accept()
#             take_screenshot(browser, 'Registration Accepted')
#
#         with allure.step('Logging out new user'):
#             logger.debug('Logging out new user')
#             register_user.logout()
#             take_screenshot(browser, 'User Logged Out')
#
#         with allure.step('Navigating back to My Account and clicking Login'):
#             logger.debug('Navigating back to My Account')
#             main_page.click_my_account()
#             logger.debug('Clicking Login')
#             main_page.click_login()
#             take_screenshot(browser, 'Main Page - Login')
#
#         with allure.step('Entering login credentials and submitting'):
#             logger.debug('Entering login credentials')
#             register_user.input_data_email()
#             register_user.input_data_passwd()
#             logger.debug('Submitting login form')
#             browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#             take_screenshot(browser, 'Login Form Submitted')
#
#         with allure.step('Checking if "My Account" link is present'):
#             logger.debug('Checking if "My Account" link is present')
#             check = WebDriverWait(browser, 2).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, "#column-right > div > a:nth-child(4)")))
#             assert check.text == 'My Account', "тест провален DUDE!!"
#             take_screenshot(browser, 'My Account Link Present')
#
#         logger.info('====== Finished: {} ======'.format(int(time.time())))
#
#     except Exception as e:
#         logger.error('Error during test execution: %s', e)
#         take_screenshot(browser, 'Error')
#         raise
