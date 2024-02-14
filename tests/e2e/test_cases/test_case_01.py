import pytest
from tests.e2e.test_cases.base_test import BaseTest
from tests.e2e.page_functions.home_page_functions import HomePageFunctions

class TestNavigation(BaseTest):
    """This class contains test for navigations to the DemoQA website"""

    @pytest.mark.smoke
    def test_navigation_to_demo_qa(self):
        """ The happy flow of navigating to DemoQA Website"""

        home_page = HomePageFunctions(self.driver)

        assert home_page.get_page_title() == "DEMOQA"
        home_page.info_log('Test Case: test_navigation_to_demo_qa executed successfully')

    def test_navigate_to_elements(self):
        """ The happy flow of navigating to DemoQA Website - Elements Page"""

        home_page = HomePageFunctions(self.driver)

        home_page.navigate_to_elements()

        assert home_page.get_current_url() == "https://demoqa.com/elements"
        home_page.info_log('Test Case: test_navigate_to_elements executed successfully')

    def test_navigate_to_forms(self):
        """ The happy flow of navigating to DemoQA Website - Forms Page"""

        home_page = HomePageFunctions(self.driver)

        home_page.navigate_to_forms()

        assert home_page.get_current_url() == "https://demoqa.com/forms"
        home_page.info_log('Test Case: test_navigate_to_forms executed successfully')

    def test_navigate_to_alerts_windows(self):
        """ The happy flow of navigating to DemoQA Website - Alerts, Frame & Windows Page"""

        home_page = HomePageFunctions(self.driver)

        home_page.navigate_to_alerts_frames_windows()

        assert home_page.get_current_url() == "https://demoqa.com/alertsWindows"
        home_page.info_log('Test Case: test_navigate_to_alerts_windows executed successfully')

    def test_navigate_to_widgets(self):
        """ The happy flow of navigating to DemoQA Website - Widgets Page"""

        home_page = HomePageFunctions(self.driver)

        home_page.navigate_to_widgets()

        assert home_page.get_current_url() == "https://demoqa.com/widgets"
        home_page.info_log('Test Case: test_navigate_to_widgets executed successfully')

    def test_navigate_to_interactions(self):
        """ The happy flow of navigating to DemoQA Website - Interaction Page"""

        home_page = HomePageFunctions(self.driver)

        home_page.navigate_to_interactions()

        assert home_page.get_current_url() == "https://demoqa.com/interaction"
        home_page.info_log('Test Case: test_navigate_to_interactions executed successfully')
