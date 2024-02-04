# This page contains configurations for the webdriver and the base test class.


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from ..configurations.config import BaseConfigs
from tests.configurations.config import BaseConfigs


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.get(BaseConfigs.url)
    driver.implicitly_wait(10)
    yield
    driver.quit()
