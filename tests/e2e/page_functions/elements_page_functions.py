# This class contains the elements page functionalities for the demoqa website


from tests.e2e.page_functions.base_page import BasePage


class ElementsPageElements():

    # navigation elements

    text_box_subpage_xpath = "//li[normalize-space()='Text Box']"
    check_box_subpage_xpath = "//li[normalize-space()='Check Box']"
    radio_button_subpage_xpath = "//li[normalize-space()='Radio Button']"
    web_tables_subpage_xpath = "//li[normalize-space()='Web Tables']"

    # text box elements
    full_name_input_xpath = "//input[@placeholder='Full Name']"
    email_input_xpath = "//input[@placeholder='name@example.com']"
    current_address_input_xpath = "//textarea[@placeholder='Current Address']"
    permanent_address_input_xpath = "//textarea[@id='permanentAddress']"
    submit_button_xpath = "//button[normalize-space()='Submit']"
    output_text_box_xpath = "//div[@id='output']"

class ElementsPageFunction(BasePage, ElementsPageElements):

    def navigate_to_text_box_subpage(self):
        self.click(ElementsPageElements.text_box_subpage_xpath)

    def navigate_to_check_box_subpage(self):
        self.click(ElementsPageElements.check_box_subpage_xpath)

    def navigate_to_radio_button_subpage(self):
        self.click(ElementsPageElements.radio_button_subpage_xpath)

    def navigate_to_web_tables_subpage(self):
        self.click(ElementsPageElements.web_tables_subpage_xpath)

    def click_submit(self):
        self.click(ElementsPageElements.submit_button_xpath)

    def input_full_name(self, full_name):
        """
        Args:
            full_name (str): full name input string
        """
        self.send_keys(ElementsPageElements.full_name_input_xpath, full_name)

    def input_email(self, email_address):
        """
        Args:
            email_address (str): email address input string
        """
        self.send_keys(ElementsPageElements.email_input_xpath, email_address)

    def input_current_address(self, current_address):
        """
        Args:
            curent_address (str): curent_address input string
        """
        self.send_keys(ElementsPageElements.current_address_input_xpath, current_address)

    def input_permanent_address(self, permanent_address):
        """
        Args:
            permanent_address (str): permanent address input string
        """
        self.send_keys(ElementsPageElements.permanent_address_input_xpath, permanent_address)

    def verify_text_box_output(self):
        """Verifying the display of the output text box
        """

        return self.is_visible(ElementsPageElements.output_text_box_xpath)
