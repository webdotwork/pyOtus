import os
import random
import time
import allure
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption(
        "--url",
        default="http://10.0.47.57:8081",
        choices=["http://10.0.47.57:8081/", "http://10.0.47.57:8081/administration/"],
        help="This is request URL"
    )
    # New option to choose between local and remote (Selenoid)
    parser.addoption(
        "--use-local",
        action="store_true",
        default=False,
        help="Use local browser instance instead of remote Selenoid"
    )

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    mobile = request.config.getoption("--mobile")
    url = request.config.getoption("--url")
    headless_mode = request.config.getoption("--headless")
    use_local = request.config.getoption("--use-local")

    # Remote Selenoid URL
    selenoid_url = "http://10.0.47.57:4444/wd/hub"

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless_mode:
            options.add_argument("--headless=new")
        if use_local:
            # Local ChromeDriver
            driver = webdriver.Chrome(options=options)
        else:
            # Remote Selenoid Chrome
            options.set_capability("selenoid:options", {
                "enableVNC": True,
                "enableVideo": True
            })
            options.browser_version = "126.0"
            driver = webdriver.Remote(
                command_executor=selenoid_url,
                options=options
            )
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless_mode:
            options.add_argument("--headless")
        if use_local:
            # Local FirefoxDriver
            driver = webdriver.Firefox(options=options)
        else:
            # Remote Selenoid Firefox
            options.set_capability("selenoid:options", {
                "enableVNC": True,
                "enableVideo": False
            })
            options.browser_version = "124.0"
            driver = webdriver.Remote(
                command_executor=selenoid_url,
                options=options
            )
    elif browser_name == "opera":
        options = webdriver.ChromeOptions()
        options.set_capability("browserName", "opera")
        if use_local:
            # Local Opera is not officially supported by Selenium WebDriver.
            # You might need to use a ChromeDriver instance and configure it for Opera.
            raise ValueError("Local Opera browser is not supported in this configuration.")
        else:
            # Remote Selenoid Opera
            options.set_capability("selenoid:options", {
                "enableVNC": True,
                "enableVideo": False
            })
            options.browser_version = "108.0"
            driver = webdriver.Remote(
                command_executor=selenoid_url,
                options=options
            )
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    caps = {
        "browserName": browser,
        # "browserVersion": version,
        # "selenoid:options": {
        #     "enableVNC": vnc,
        #     "name": request.node.name,
        #     "screenResolution": "1280x2000",
        #     "enableVideo": video,
        #     "enableLog": logs,
        #     "timeZone": "Europe/Moscow",
        #     "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
        # },
        # "acceptInsecureCerts": True,
    }

    for k, v in caps.items():
        options.set_capability(k, v)
    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )
    # driver.maximize_window()

    # request.addfinalizer(driver.close)
    if not mobile:
        driver.maximize_window()

        driver.quit()

    # driver.get(url)
    # driver.url = url
    request.addfinalizer(finalizer)
    return driver
