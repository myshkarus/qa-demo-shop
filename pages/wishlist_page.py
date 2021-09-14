import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from constants.wishlist_page import WishlistPageConstants
from helpers.base import BaseHelpers
from pages.header_panel import HeaderPanel
from pages.navigation_panel import NavigationPanel


class WishlistPage(BaseHelpers):
    """Store helper methods related to WishlistPage object actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = WishlistPageConstants
        self.navigation_panel = NavigationPanel(self.driver)
        self.header_panel = HeaderPanel(self.driver)

    def clean_wishlist(self):
        """Remove all items persisted in wishlist"""

        # Open Wishlist Page
        self.header_panel.goto_wishlist_page()

        # Check if wishlist is not empty
        empty = self.verify_wishlist_is_empty(text=self.const.MSG_WISHLIST_EMPTY_TEXT)

        if not empty:
            # Select all items if any
            items_in_wishlist = self.wait_until_elements_find(locator_type=By.XPATH,
                                                              locator=self.const.TABLE_ROWS_ITEM_XPATH)
            if len(items_in_wishlist):
                for row in items_in_wishlist:
                    row.find_element(By.XPATH, self.const.INPUT_CHECKBOX_REMOVE_ITEM_XPATH).click()
                self.wait_and_click(locator_type=By.XPATH, locator=self.const.BUTTON_UPDATE_WISHLIST_XPATH)

    def verify_wishlist_is_empty(self, text=""):
        """Find message on wishlist status and assert text"""
        text = self.const.MSG_WISHLIST_EMPTY_TEXT
        try:
            assert self.is_text_exists(locator_type=By.XPATH, locator=self.const.LOCATOR_BY_TEXT.format(text=text),
                                       text=text)
            return True
        except Exception as err:
            return False

    def add_product_to_wishlist(self):
        """Take selected products and add them to wishlist"""
        departments_to_visit = self.navigation_panel.random_departments()
        self.header_panel.goto_home_page()

        for department in departments_to_visit:
            self.wait_and_click(locator_type=By.XPATH, locator=department[1])
            if department[0] == 'BOOKS':
                from pages.books_page import BooksPage
                books_page = BooksPage(self.driver)
                books_page.add_to_wishlist()
            self.header_panel.goto_home_page()
        return WishlistPage(self.driver)
