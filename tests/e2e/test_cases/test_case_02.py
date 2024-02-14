import pytest
from tests.e2e.test_cases.base_test import BaseTest
from tests.e2e.page_functions.home_page_functions import HomePageFunctions
from tests.e2e.page_functions.elements_page_functions import ElementsPageFunction
from faker import Faker


fake = Faker()

class TestElementsPage(BaseTest):
    """This class contains the test cases for navigation of the Elements Page subpages for DemoQA

    Args:
        BaseTest (Class): Parent Class containing inheritance of conftest.py
    """

    def test_navigate_to_text_box_subpage(self):
        """Success flow of navigating to the text box subpage
        """

        # Arrange
        home_page = HomePageFunctions(self.driver)
        elements_page = ElementsPageFunction(self.driver)

        home_page.navigate_to_elements()

        page_header = "Text Box"

        # Act
        elements_page.navigate_to_text_box_subpage()

        # Assert
        assert elements_page.get_main_header_text() == page_header

class TestElementsTextBoxSubpage(BaseTest):
    """This class contains the test cases for the Text Box Subpage for DemoQA
    Args:
        BaseTest (Class): Parent Class containing inheritance of conftest.py
    """

    @pytest.mark.critical
    @pytest.mark.smoke
    def test_successful_submission(self):
        """Test Case verifies valid submissions for the text box subpage
        """

        # Arrange
        home_page = HomePageFunctions(self.driver)
        elements_page = ElementsPageFunction(self.driver)

        home_page.navigate_to_elements()
        elements_page.navigate_to_text_box_subpage()

        # TODO: add a separate test data file
        valid_name = 'John Doe'
        valid_email = 'johndoe@example.com'
        valid_address = fake.address()
        permanent_address = fake.address()

        # Act
        elements_page.input_full_name(valid_name)
        elements_page.input_email(valid_email)
        elements_page.input_current_address(valid_address)
        elements_page.input_permanent_address(permanent_address)
        elements_page.click_submit()

        # Assert

        assert elements_page.verify_text_box_output()
