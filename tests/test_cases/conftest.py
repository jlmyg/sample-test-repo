# This page contains configurations for the webdriver and the base test class.


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.configurations.config import Configs


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.get(Configs.url)
    yield
    driver.quit()
