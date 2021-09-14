import logging

from selenium.webdriver.common.by import By

from constants.register_page import RegisterPageConstants
from helpers.base import BaseHelpers, CustomerData
from pages.header_panel import HeaderPanel


class RegisterPage(BaseHelpers):
    """Store helper methods related to RegisterPage object actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = RegisterPageConstants
        self.header_panel = HeaderPanel(self.driver)

    def register_new_customer(self, customer: CustomerData):
        """Fill registration form fields and press Register button"""

        # Fill in required fields
        self.fill_in_registration_form(customer=customer)

        # Click on Register button
        register_page = self.click_register_button()
        return register_page

    def fill_in_registration_form(self, customer: CustomerData):
        """Fill in registration form fields"""

        # Clear and fill required fields
        if customer.gender == 'male':
            self.wait_and_click(locator_type=By.XPATH, locator=self.const.INPUT_RADIO_GENDER_MALE_XPATH)
        elif customer.gender == 'female':
            self.wait_and_click(locator_type=By.XPATH, locator=self.const.INPUT_RADIO_GENDER_FEMALE_XPATH)

        self.fill_input_field(by=By.XPATH, locator=self.const.INPUT_FIELD_FIRST_NAME_XPATH, value=customer.first_name)
        self.fill_input_field(by=By.XPATH, locator=self.const.INPUT_FIELD_LAST_NAME_XPATH, value=customer.last_name)
        self.fill_input_field(by=By.XPATH, locator=self.const.INPUT_FIELD_EMAIL_XPATH, value=customer.email)
        self.fill_input_field(by=By.XPATH, locator=self.const.INPUT_FIELD_PASSWORD_XPATH, value=customer.password)
        self.fill_input_field(by=By.XPATH, locator=self.const.INPUT_FIELD_CONFIRM_PASSWORD_XPATH,
                              value=customer.password)
        self.log.debug(
            f"Fields are filled with invalid values: \ngender:{customer.gender}, \nfirst_name:{customer.first_name},"
            f"\nlast_name:{customer.last_name}, \nemail:{customer.email}, \npassword: {customer.password}")
        return RegisterPage(self.driver)

    def click_register_button(self):
        """Click on Register button"""

        # Click on Register button
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.BUTTON_REGISTER_XPATH)
        self.log.info("Clicked on Register button")
        return RegisterPage(self.driver)

    def validate_register_fields(self, error_text):
        """Click on Register button and validate the correctness of values"""

        # Click on Register button
        self.click_register_button()

        # Check whether error message appears
        self.verify_message(text=error_text)

    def verify_success_registration(self):
        """Verify that message on success registration is on Register  Page"""
        # Find success message on Register Page
        message = self.const.SUCCESS_REGISTRATION_TEXT
        assert self.is_text_exists(locator_type=By.XPATH, locator=self.const.LOCATOR_BY_TEXT.format(text=message),
                                   text=message)
        self.log.debug(f"Text='{self.const.SUCCESS_REGISTRATION_TEXT}' is not located")

        # Click on Continue button
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.BUTTON_CONTINUE_XPATH)

    def verify_required_fields(self, error_text):
        """Verify whether required fields are empty and find error message"""

        # Click on Register button
        self.click_register_button()

        # Check whether error message appears
        self.verify_message(text=error_text)

    def verify_account_already_exists(self):
        """Verify whether account is already exists"""

        # Click on Register button
        self.click_register_button()

        # Check whether error message appears
        self.verify_message(text=self.const.MSG_ACCOUNT_ALREADY_EXISTS_TEXT)
        self.log.info("The specified account already exists")

    def verify_new_customer_is_logged_into_account(self, customer: CustomerData):
        """Find customer email within the header and compare customer details with data on CustomerAccountPage"""

        self.header_panel.verify_customer_login_in_header_panel(customer=customer)
        active_account = self.header_panel.goto_customer_account_page(customer=customer)
        active_account.open_customer_info_and_verify()

    def verify_message(self, text):
        """Find error message and assert text"""

        assert self.is_text_exists(locator_type=By.XPATH, locator=self.const.LOCATOR_BY_TEXT.format(text=text),
                                   text=text)

