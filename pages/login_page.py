import logging

from selenium.webdriver.common.by import By

from constants.login_page import LoginPageConstants
from helpers.base import BaseHelpers, CustomerData
from pages.header_panel import HeaderPanel


class LoginPage(BaseHelpers):
    """Store helper methods related to LoginPage object actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = LoginPageConstants
        self.header_panel = HeaderPanel(self.driver)

    def login_customer(self, customer: CustomerData):
        """Provide credentials and press Log In button to login"""

        # Fill in required fields
        self.fill_in_login_form(customer=customer)
        self.log.info("Login form's fields are filled in")

        # Click on Log In button
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.BUTTON_LOGIN_XPATH)
        self.log.info("Clicked on 'Log In' button")
        self.header_panel.verify_customer_login_in_header_panel(customer=customer)
        from pages.home_page import HomePage
        return HomePage(self.driver)

    def fill_in_login_form(self, customer: CustomerData):
        """Fill in login form fields"""

        # Clear and fill required fields
        self.fill_input_field(by=By.XPATH, locator=self.const.INPUT_FIELD_EMAIL_XPATH, value=customer.email)
        self.fill_input_field(by=By.XPATH, locator=self.const.INPUT_FIELD_PASSWORD_XPATH, value=customer.password)
        self.log.debug(
            f"Fields are filled with invalid values => email:{customer.email}, password: {customer.password} ")
        return LoginPage(self.driver)

    def verify_customer_is_logged_in_account(self, customer: CustomerData):
        """Find customer email within the header and compare customer details with data on CustomerAccountPage"""

        self.header_panel.verify_customer_login_in_header_panel(customer=customer)
        active_account = self.header_panel.goto_customer_account_page(customer=customer)
        active_account.open_customer_info_and_verify()

    def validate_login_fields(self, error_text):
        """Click on Log In button and validate the correctness of values"""
        # Click on Log In button
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.BUTTON_LOGIN_XPATH)
        self.log.info("Clicked on 'Log In' button")

        # Check whether error message appears
        self.verify_message(text=error_text)

    def verify_message(self, text):
        """Find error message and assert text"""
        assert self.is_text_exists(locator_type=By.XPATH, locator=self.const.LOCATOR_BY_TEXT.format(text=text),
                                   text=text)
