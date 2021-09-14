import logging

from selenium.webdriver.common.by import By

from constants.books_page import BooksPageConstants
from helpers.base import BaseHelpers
from pages.navigation_panel import NavigationPanel


class BooksPage(BaseHelpers):
    """Store helper methods related to BooksPage object actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = BooksPageConstants
        self.navigation_panel = NavigationPanel(driver)

    def add_to_wishlist(self):
        """Add selected products to wishlist"""
        # Go go Books Page
        self.wait_and_click(By.XPATH, self.navigation_panel.const.LINK_NAV_BOOKS_XPATH)

        # Add product 1 to the wishlist
        self.wait_until_element_find(locator_type=By.XPATH, locator=self.const.LOCATOR_BY_TEXT.format(
            text=self.const.BOOK_PRODUCT_HEALTH_TEXT)).click()
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.BUTTON_ADD_TO_WISHLIST_XPATH)

        # Return to Books Page
        self.wait_and_click(By.XPATH, self.navigation_panel.const.LINK_NAV_BOOKS_XPATH)
        self.wait_until_element_find(locator_type=By.XPATH, locator=self.const.LOCATOR_BY_TEXT.format(
            text=self.const.BOOK_PRODUCT_FICTION_TEXT)).click()
        self.wait_and_click(locator_type=By.XPATH, locator=self.const.BUTTON_ADD_TO_WISHLIST_XPATH)
        return BooksPage(self.driver)