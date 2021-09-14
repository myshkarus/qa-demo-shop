import logging

from constants.home_page import HomePageConstants
from helpers.base import BaseHelpers
from pages.header_panel import HeaderPanel


class HomePage(BaseHelpers):
    """Store helper methods related to HomePage object actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = HomePageConstants
        self.header_panel = HeaderPanel(self.driver)
