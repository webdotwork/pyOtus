import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption(
        "--url",
        default="http://10.0.47.57:8081",
        choices=["http://10.0.47.57:8081", "http://10.0.47.57:8081/administration/"],
        help="This is request URL"
    )

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless_mode = request.config.getoption("--headless")

    selenoid_url = "http://10.0.47.57:4444/wd/hub"

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless_mode:
            options.add_argument("headless=new")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
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

    driver.maximize_window()

    request.addfinalizer(driver.quit)

    driver.get(url)
    driver.url = url

    return driver
