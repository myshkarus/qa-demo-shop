import logging

from constants.search_page import SearchPageConstants
from helpers.base import BaseHelpers


class SearchPage(BaseHelpers):
    """Store helper methods related to SearchPage object actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = SearchPageConstants
