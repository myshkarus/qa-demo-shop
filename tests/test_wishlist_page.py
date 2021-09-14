"""Store tests related to Wishlist Page"""

import pytest

from conftest import BaseTest
from constants.base import BaseConstants
from helpers.base import create_driver


@pytest.mark.parametrize('browser_name', [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestWishlistPage(BaseTest):

    @pytest.fixture(scope='function')
    def driver(self, browser_name):
        driver = create_driver(browser_name)
        yield driver
        driver.close()

    def test_clean_wishlist(self, register_page, customer, logout):
        """
        - Register new customer
        - Add products to wishlist and verify wishlist is not empty
        - Clean wishlist
        - Verify wishlist is empty
        """

        # Register new customer
        register_page.register_new_customer(customer=customer)
        self.log.info("New customer is registered")

        # Add products to wishlist
        wishlist_page = register_page.header_panel.goto_wishlist_page()
        wishlist_page.add_product_to_wishlist()
        self.log.info("Product are added to wishlist")
        assert not wishlist_page.verify_wishlist_is_empty()
        self.log.info("Verified wishlist is not empty")

        # Clean wishlist
        wishlist_page.clean_wishlist()
        self.log.info("Wishlist is cleaned")

        # Verify wishlist is empty
        wishlist_page.verify_wishlist_is_empty()
        self.log.info("Verified wishlist is empty")
