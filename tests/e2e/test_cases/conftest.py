# This page contains configurations for the webdriver and the base test class.


import pytest
from datetime import datetime
from pytest_html_reporter import attach
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.e2e.configurations.config import BaseConfigs


@pytest.fixture(scope="function")
def driver_init(request: pytest.FixtureRequest):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
