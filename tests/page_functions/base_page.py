# This class contains base actions for all the page functionalities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 



class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.get_element(by_locator).click()

    def get_current_url(self):
        return self.driver.title