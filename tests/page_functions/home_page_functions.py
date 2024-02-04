# This class contains the homepage functionalities for the demoqa website


from tests.page_functions.base_page import BasePage

class HomePageElements():

    elements_xpath =  "//h5[normalize-space()='Elements']"


class HomePageFunctions(BasePage, HomePageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_elements(self):
        self.click(HomePageElements.elements_xpath)