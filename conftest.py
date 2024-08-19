# import datetime
# import allure
# import logging
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.service import Service as FFService
# from selenium.webdriver.firefox.options import Options as FFOptions
#
#
# def pytest_addoption(parser):
#     parser.addoption("--launch_mode", default="remote", choices=["remote", "local"])
#     parser.addoption("--browser_local", default="ch", choices=["ch", "ff"])
#     parser.addoption("--browser_remote", default="chrome", choices=["chrome", "firefox"])
#     parser.addoption("--bv_remote", action="store", default="125.0")
#     parser.addoption("--vnc", action="store_true")
#     parser.addoption("--executor", action="store", default="127.0.0.1")
#     parser.addoption("--headless", action="store_true")
#     parser.addoption("--url", action="store", default="http://10.0.47.57:8081")
#     parser.addoption("--log_level", action="store", default="INFO")
#
#
# @pytest.fixture
# def browser(request):
#     launch_mode = request.config.getoption("--launch_mode")
#     browser_local = request.config.getoption("--browser_local")
#     headless_mode = request.config.getoption("--headless")
#     url = request.config.getoption("--url")
#
#     browser_remote = request.config.getoption("--browser_remote")
#     bv_remote = request.config.getoption("--bv_remote")
#     vnc = request.config.getoption("--vnc")
#     executor = request.config.getoption("--executor")
#     executor_url = f"http://{executor}:4444/wd/hub"
#
#     if launch_mode == "local":
#         if browser_local == "ch":
#             options = ChromeOptions()
#             if headless_mode:
#                 options.add_argument("--headless=new")
#             browser = webdriver.Chrome(service=ChromeService(), options=options)
#         elif browser_local == "ff":
#             options = FFOptions()
#             if headless_mode:
#                 options.headless = True
#             browser = webdriver.Firefox(service=FFService(), options=options)
#
#     elif launch_mode == "remote":
#         if browser_remote == "chrome":
#             options_remote = ChromeOptions()
#         elif browser_remote == "firefox":
#             options_remote = FFOptions()
#
#         if headless_mode and browser_remote == "chrome":
#             options_remote.add_argument("--headless=new")
#         elif headless_mode and browser_remote == "firefox":
#             options_remote.headless = True
#
#         caps = {
#             "browserName": browser_remote,
#             # "browserVersion": bv_remote,
#             # "selenoid:options": {
#             #     "enableVNC": vnc,
#             #     "enableVideo": False,  # Adjust according to your need
#             #     "enableLog": True,     # Adjust according to your need
#             #     "name": request.node.name
#             # }
#         }
#
#         for k, v in caps.items():
#             options_remote.set_capability(k, v)
#
#         browser = webdriver.Remote(
#             command_executor=executor_url,
#             options=options_remote
#         )
#
#     browser.maximize_window()
#     browser.get(url)
#
#     def fin():
#         browser.quit()
#
#     request.addfinalizer(fin)
#
#     return browser



import os
import random
import time
import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


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
        choices=["http://10.0.47.57:8081", "http://10.0.47.57:8081/administration/"], # pytest --url http://10.0.47.57:8081/administration/ tests/test_add_new_goods.py tests/test_del_goods.py
        help="This is request url"
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

    executor_url = f"http://{executor}:4444/wd/hub"

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

    def finalizer():
        # video_url = f"http://{executor}:8080/video/{driver.session_id}.mp4"
        #
        # if request.node.status == "failed":
        #     if video:
        #         allure.attach(
        #             body=wait_url_data(video_url),
        #             name="video_for_" + driver.session_id,
        #             attachment_type=allure.attachment_type.MP4,
        #         )
        #
        # if video and wait_url_data(video_url):
        #     requests.delete(url=video_url)

        driver.quit()

    # driver.get(url)
    # driver.url = url
    request.addfinalizer(finalizer)
    return driver
