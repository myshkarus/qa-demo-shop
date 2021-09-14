import logging

from selenium.webdriver.common.by import By

from constants.header_panel import HeaderPanelConstants
from helpers.base import BaseHelpers, CustomerData


class HeaderPanel(BaseHelpers):
    """Store helper methods related to Header Panel actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = HeaderPanelConstants

    def goto_home_page(self):
        """Click on header logo and return HomePage object"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.LINK_HOME_PAGE_XPATH)
        from pages.home_page import HomePage
        return HomePage(self.driver)

    def goto_register_page(self):
        """Click on register link and return RegisterPage object"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.LINK_REGISTER_XPATH)
        from pages.register_page import RegisterPage
        return RegisterPage(self.driver)

    def goto_login_page(self):
        """Click on login link and return LoginPage object"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.LINK_LOGIN_XPATH)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)

    def goto_cart_page(self):
        """Click on cart link and return CartPage object"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.LINK_CART_XPATH)
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def goto_wishlist_page(self):
        """Click on wishlist link and return WishlistPage object"""
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.LINK_WISHLIST_XPATH)
        from pages.wishlist_page import WishlistPage
        return WishlistPage(self.driver)

    def goto_customer_account_page(self, customer: CustomerData):
        """Click on active customer link and return CustomerAccountPage object"""
        self.wait_until_element_find(locator_type=By.XPATH,
                                     locator=self.const.LINK_LOGGED_IN_CUSTOMER_XPATH.format(
                                         email_lower=customer.email.lower())).click()
        from pages.customer_account_page import CustomerAccountPage
        return CustomerAccountPage(driver=self.driver, customer=customer)

    def logout_customer(self):
        """Click on logout and return HomePage object"""

        self.wait_and_click(locator_type=By.XPATH, locator=self.const.LINK_LOGOUT_XPATH)
        from pages.home_page import HomePage
        return HomePage(self.driver)

    def verify_customer_login_in_header_panel(self, customer: CustomerData):
        """Find customer login within the header_panel"""

        assert self.wait_until_element_find(locator_type=By.XPATH,
                                            locator=self.const.LINK_LOGGED_IN_CUSTOMER_XPATH.format(
                                                email_lower=customer.email.lower()))
        self.log.debug(f"Account {customer.email} is not found in the header_panel")
