"""Store tests related to Login Page"""

import pytest

from conftest import BaseTest
from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from helpers.base import CustomerData, create_driver


@pytest.mark.parametrize('browser_name', [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestLoginPage(BaseTest):

    @pytest.fixture(scope='function')
    def driver(self, browser_name):
        driver = create_driver(browser_name)
        yield driver
        driver.close()

    def test_successful_login(self, login_page, returning_customer, logout):
        """
        - Fill in email and password fields and click on Log In button
        - Verify that returning customer is logged in successfully
        """

        # Fill in email and password fields and click on Log In button
        login_page.login_customer(returning_customer)
        self.log.info("Required fields are filled in and Log In button is pressed")

        # Verify successful login
        login_page.verify_customer_is_logged_in_account(returning_customer)
        self.log.info(f"Returning customer with email: {returning_customer.email} logged in successfully")

    @pytest.mark.parametrize('data', [{'guest': CustomerData(email='comeandgo123@mail.com', password='2327979749797'),
                                       'error': LoginPageConstants.MSG_NO_CUSTOMER_ACCOUNT_FOUND_TEXT},
                                      {'guest': CustomerData(password='2327979749797'),
                                       'error': LoginPageConstants.MSG_NO_CUSTOMER_ACCOUNT_FOUND_TEXT},
                                      {'guest': CustomerData(email='wrongemail@somedomain', password='customer2345'),
                                       'error': LoginPageConstants.MSG_INCORRECT_EMAIL_TEXT},
                                      {'guest': CustomerData(email=LoginPageConstants.REGISTERED_CUSTOMER_EMAIL),
                                       'error': LoginPageConstants.MSG_INCORRECT_CREDENTIALS_TEXT},
                                      {'guest': CustomerData(),
                                       'error': LoginPageConstants.MSG_UNSUCCESSFUL_LOGIN_TEXT},
                                      ])
    def test_empty_registration_fields(self, login_page, data):
        """
        - Fill in login form with incomplete data
        - Click Log In button and verify error message
        """
        # Fill in login fields
        login_page.fill_in_login_form(customer=data['guest'])
        self.log.info(f"Login form is filled with data: email={data['guest'].email}, password={data['guest'].password}")

        # Click Log In button and verify error message
        login_page.validate_login_fields(error_text=data['error'])
        self.log.info("Verified error message '%s'", data['error'])
