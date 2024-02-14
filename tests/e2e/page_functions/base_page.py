# This class contains base actions for all the page functionalities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tests.e2e.configurations.logger import LogGen

logger = LogGen.loggen()

class BaseElements():
    """This class contains repeated generic elements from demoQA
    """

    page_main_header = "//div[@class='main-header']"

class BasePage(BaseElements):

    def __init__(self, driver):
        self.driver = driver

    def info_log(self, msg):
        "Used to log information"
        logger.info(msg)

    def error_log(self, msg):
        "Used to log errors"
        logger.error(msg)

    def xpath_to_tuple(self, xpath):
        return (By.XPATH, xpath)

    def get_element(self, xpath):
        try:
            self.info_log('Finding locator {}'.format(xpath))
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.xpath_to_tuple(xpath)))
        except TimeoutException:
            self.error_log('Locator {} does not exist'.format(xpath))

    def click(self, xpath):
        self.get_element(xpath).click()

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def send_keys(self, xpath, string):
        self.get_element(xpath).send_keys(string)

    def get_main_header_text(self):
        return self.get_element(BaseElements.page_main_header).text

    def is_visible(self, xpath):

        try:
            return bool(self.get_element(xpath))
        except TimeoutException:
            self.error_log('element {} is not visible'.format(xpath))
            return False
