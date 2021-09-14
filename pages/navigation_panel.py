import logging
import random

from constants.navigation_panel import NavigationPanelConstants
from helpers.base import BaseHelpers


class NavigationPanel(BaseHelpers):
    """Store helper methods related to Navigation Panel actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.const = NavigationPanelConstants
        self.departments = []

    def random_departments(self, to_visit=2):
        departments = random.sample(self.const.departments, k=to_visit)
        return departments
