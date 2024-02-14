# This class contains the homepage functionalities for the demoqa website


from tests.e2e.page_functions.base_page import BasePage

class HomePageElements():

    elements_xpath = "//h5[normalize-space()='Elements']"
    forms_xpath = "//h5[normalize-space()='Forms']"
    alerts_frames_windows_xpath = "//h5[normalize-space()='Alerts, Frame & Windows']"
    widgets_xpath = "//h5[normalize-space()='Widgets']"
    interactions_xpath = "//h5[normalize-space()='Interactions']"


class HomePageFunctions(BasePage, HomePageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_elements(self):
        self.click(HomePageElements.elements_xpath)

    def navigate_to_forms(self):
        self.click(HomePageElements.forms_xpath)

    def navigate_to_alerts_frames_windows(self):
        self.click(HomePageElements.alerts_frames_windows_xpath)

    def navigate_to_widgets(self):
        self.click(HomePageElements.widgets_xpath)

    def navigate_to_interactions(self):
        self.click(HomePageElements.interactions_xpath)
