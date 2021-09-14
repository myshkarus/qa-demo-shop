"""Store tests related to Register Page"""

import pytest

from conftest import BaseTest
from constants.base import BaseConstants
from constants.register_page import RegisterPageConstants
from helpers.base import CustomerData, create_driver


@pytest.mark.parametrize('browser_name', [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestRegisterPage(BaseTest):

    @pytest.fixture(scope='function')
    def driver(self, browser_name):
        driver = create_driver(browser_name)
        yield driver
        driver.close()

    def test_customer_registration(self, customer: CustomerData, register_page, logout):
        """
        - Fill in registration fields with valid values and click on Register button
        - Verify that registration is successful
        - Verify new customer data appear in customer account
        """

        # Fill in registration fields and click on Register button
        register_page = register_page.register_new_customer(customer=customer)
        self.log.info("Required fields are filled in and Register button is pressed")

        # Verify success registration
        register_page.verify_success_registration()
        self.log.info("New customer is registered successfully")

        # Verify new customer data appears in customer account
        register_page.verify_new_customer_is_logged_into_account(customer=customer)
        self.log.info("Verified that customer's data are in customer account")

    def test_returning_customer_reregistration(self, returning_customer: CustomerData, register_page):
        """
        - Fill in registration fields with returning customer data
        - Click Register button and verify that account already exists
        """

        # Fill in register fields with all required values
        register_page.fill_in_registration_form(customer=returning_customer)
        self.log.info("Required fields are filled in with data of returning customer")

        # Click on Register button and validate values in fields
        register_page.verify_account_already_exists()
        self.log.info("Error message match to expected")

    @pytest.mark.parametrize('data', [(CustomerData(last_name='Doe', email='j.doe@mail.com', password='abc123'),
                                       RegisterPageConstants.MSG_FIRST_NAME_REQUIRED_TEXT),
                                      (CustomerData(first_name='John', email='j.doe@mail.com', password='abc123'),
                                       RegisterPageConstants.MSG_LAST_NAME_REQUIRED_TEXT),
                                      (CustomerData(first_name='John', last_name='Doe', password='abc123'),
                                       RegisterPageConstants.MSG_EMAIL_REQUIRED_TEXT),
                                      (CustomerData(first_name='John', last_name='Doe', email='j.doe@mail.com'),
                                       RegisterPageConstants.MSG_PASSWORD_REQUIRED_TEXT)])
    def test_required_fields(self, data, register_page):
        """
        - Fill in register form with incomplete data
        - Click Register button and verify error message
        """
        # Fill in registration fields
        register_page.fill_in_registration_form(customer=data[0])
        self.log.info(f"Register form is filled in with incomplete customer data")

        # Click Log In button and verify error message
        register_page.verify_required_fields(error_text=data[1])
        self.log.info("Verified error message '%s'", data[1])
