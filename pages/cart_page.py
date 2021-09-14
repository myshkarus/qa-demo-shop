import logging

from constants.cart_page import CartPageConstants
from helpers.base import BaseHelpers


class CartPage(BaseHelpers):
    """Store helper methods related to CartPage object actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = CartPageConstants
