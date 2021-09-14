import os


class BaseConstants:
    """Store common constants of test framework"""

    HEADLESS_MODE = True
    START_PAGE_URL = "http://demowebshop.tricentis.com/"

    CHROME = 'chrome'
    FIREFOX = 'firefox'

    current_module = os.path.dirname(os.path.abspath(__file__))
