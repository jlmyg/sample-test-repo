# This page contains configurations for the webdriver and the base test class.


import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.e2e.configurations.config import BaseConfigs

@pytest.fixture(scope='function')
def driver_init(headless, request: pytest.FixtureRequest):

    options = webdriver.ChromeOptions()
    chrome_prefs = {}
    options.experimental_options["prefs"] = chrome_prefs
    if headless.lower() == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--dist=loadfile")
        options.add_argument("window-size=1920,1080")
        options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    request.cls.driver = driver
    driver.get(BaseConfigs.url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    collect_screenshot(driver, request)
    driver.close()

def collect_screenshot(driver, request):
    """Method is called during teardown to collect screenshots"""
    currentdatetime = datetime.now().strftime(("%m_%d_%y_%X"))
    currentdatestring = currentdatetime.replace(":", "_")
    screenshotname = f"{request.node.originalname}_{currentdatestring}"
    driver.save_screenshot('./reports/screenshots/{}.png'.format(screenshotname))

def pytest_addoption(parser: pytest.Parser):
    """Add additional terminal params here
    """
    parser.addoption("--headless", action="store", default="false", help="parameter in setting up headless browser")

@pytest.fixture()
def headless(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--headless")
