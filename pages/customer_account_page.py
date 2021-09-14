import logging

from selenium.webdriver.common.by import By

from constants.customer_account_page import CustomerAccountPageConstants
from helpers.base import BaseHelpers
from pages.header_panel import HeaderPanel


class CustomerAccountPage(BaseHelpers):
    """Store helper methods related to CustomerAccountPage object actions"""

    def __init__(self, driver, customer=None):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = CustomerAccountPageConstants
        self.header_panel = HeaderPanel(self.driver)
        self.customer = customer

    def open_customer_info_and_verify(self):
        """Click on customer link in the header and open CustomerAccountPage"""

        self.wait_until_element_find(locator_type=By.XPATH, locator=self.const.LINK_CUSTOMER_INFO_XPATH).click()
        self.verify_customer_account_is_active()
        return CustomerAccountPage(self.driver)

    def verify_customer_account_is_active(self):
        """Verify that details on CustomerAccountPage is the same as customer daa"""

        field_first_name = self.wait_until_element_find(locator_type=By.XPATH,
                                                        locator=self.const.INPUT_FIELD_FIRST_NAME_XPATH)
        assert field_first_name.get_attribute("value") == self.customer.first_name

        field_last_name = self.wait_until_element_find(locator_type=By.XPATH,
                                                       locator=self.const.INPUT_FIELD_LAST_NAME_XPATH)
        assert field_last_name.get_attribute("value") == self.customer.last_name

        field_email = self.wait_until_element_find(locator_type=By.XPATH,
                                                   locator=self.const.INPUT_FIELD_EMAIL_XPATH)
        assert field_email.get_attribute("value") == self.customer.email

        if self.customer.gender == 'male':
            assert self.is_checked(locator_type=By.XPATH, locator=self.const.INPUT_RADIO_GENDER_MALE_XPATH)
        elif self.customer.gender == 'female':
            assert self.is_checked(locator_type=By.XPATH, locator=self.const.INPUT_RADIO_GENDER_FEMALE_XPATH)

        self.log.info(f"Verified that customer account {self.customer.email} is activated")
