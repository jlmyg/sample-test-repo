import pytest

from  tests.test_cases.base_test import BaseTest

from tests.page_functions.home_page_functions import HomePageFunctions

class TestNavigation(BaseTest):
    """This class contains test for navigating to the DemoQA website"""


    def test_navigation_to_demo_qa(self):
        """ The happy flow of navigating to DemoQA Website"""

        home_page = HomePageFunctions(self.driver)

        assert home_page.get_current_url() == "DEMOQA"