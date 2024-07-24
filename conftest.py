import pytest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption(
        "--url",
        default="http://10.0.47.57:8081",
        choices=["http://10.0.47.57:8081", "http://10.0.47.57:8081/administration/"], # pytest --url http://10.0.47.57:8081/administration/ tests/test_add_new_goods.py tests/test_del_goods.py
        help="This is request url"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless_mode = request.config.getoption("--headless")


    if browser_name == "chrome":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=ChromiumService(), options=options)
    elif browser_name == "firefox":
        # service = FFService(executable_path="/snap/bin/geckodriver") Для ubuntu 22.04
        driver = webdriver.Firefox(options=FFOptions(), service=FFService())
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
