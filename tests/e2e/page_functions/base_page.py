# This class contains base actions for all the page functionalities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def xpath_to_tuple(self, xpath):
        return (By.XPATH, xpath)

    def get_element(self, xpath):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.xpath_to_tuple(xpath)))

    def click(self, xpath):
        self.get_element(xpath).click()

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def send_keys(self, xpath, string):
        self.get_element(xpath).send_keys(string)
