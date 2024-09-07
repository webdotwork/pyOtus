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

    driver.maximize_window()

    request.addfinalizer(driver.quit)

    driver.get(url)
    driver.url = url

    return driver
