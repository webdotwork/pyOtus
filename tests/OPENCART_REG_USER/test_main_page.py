import pytest
import allure
import logging
import time
from page_objects.main_page import MainPage


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def take_screenshot(browser, name):
    allure.attach(browser.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)


@pytest.mark.usefixtures("browser")
def test_navigate_to_login_page(browser):
    logger.info('====== Started: {} ======'.format(int(time.time())))
    try:
        with allure.step('Navigating to Main Page and clicking My Account'):
            logger.debug('Navigating to Main Page')
            main_page = MainPage(browser)
            main_page.click_my_account()
            take_screenshot(browser, 'Clicked My Account')

        with allure.step('Navigating to Login Page'):
            logger.debug('Clicking Login')
            main_page.click_login()
            take_screenshot(browser, 'Clicked Login')

        with allure.step('Checking URL'):
            assert "account/login" in browser.current_url, "Not on the login page."
            take_screenshot(browser, 'Login Page URL Verified')

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        take_screenshot(browser, 'Error')
        raise


@pytest.mark.usefixtures("browser")
@pytest.mark.parametrize("link_text, expected_url_part", [
    # ("My Account", "account/account"),
    ("Register", "/register"),
    ("Login", "/login")
])
def test_navigation_links(browser, link_text, expected_url_part):
    logger.info('====== Started: {} ======'.format(int(time.time())))
    try:
        with allure.step(f'Navigating to Main Page and clicking {link_text}'):
            logger.debug('Navigating to Main Page')
            main_page = MainPage(browser)

            # if link_text == "My Account":
            main_page.click_my_account()
            if link_text == "Register":
                main_page.click_register_user()
            elif link_text == "Login":
                main_page.click_login()
            take_screenshot(browser, f'Clicked {link_text}')

        with allure.step(f'Checking URL for {link_text}'):
            assert expected_url_part in browser.current_url, f"Navigation to {link_text} failed."
            take_screenshot(browser, f'{link_text} URL Verified')

        logger.info('====== Finished: {} ======'.format(int(time.time())))

    except Exception as e:
        logger.error('Error during test execution: %s', e)
        take_screenshot(browser, 'Error')
        raise