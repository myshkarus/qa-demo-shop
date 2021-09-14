import logging
import random
import time
from collections import namedtuple

from constants.base_text import Names

import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from constants.base import BaseConstants


def wait_until_ok(timeout, period=0.25):
    """Repeat call of decorated function until it is OK or timeout is reached"""

    def actual_decorator(target_func):
        logger = logging.getLogger(__name__)

        def wrapper(*args, **kwargs):
            must_end = time.time() + timeout
            while True:
                try:
                    return target_func(*args, **kwargs)
                except (WebDriverException, AssertionError, TimeoutException) as error:
                    error_name = error if str(error) else error.__class__.__name__
                    logger.debug("Catch %s. Left %s seconds", error_name, (must_end - time.time()))
                    if time.time() >= must_end:
                        logger.warning("Waiting timed out after %s", timeout)
                        raise error
                    time.sleep(period)

        return wrapper

    return actual_decorator


def log_action(target_func):
    """Logger decorator"""

    logger = logging.getLogger("action_decorator")

    def wrapper(*args, **kwargs):
        logger.debug(f"{target_func.__doc__}: {args}; {kwargs}")
        return target_func(*args, **kwargs)

    return wrapper


def create_driver(browser_name):
    """Create driver based on browser name"""
    if browser_name == BaseConstants.CHROME:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        if BaseConstants.HEADLESS_MODE:
            return webdriver.Chrome(options=options)
        else:
            return webdriver.Chrome()
    elif browser_name == BaseConstants.FIREFOX:
        options = Options()
        options.add_argument('--headless')
        if BaseConstants.HEADLESS_MODE:
            return webdriver.Firefox(options=options)
        else:
            return webdriver.Firefox()
    else:
        raise ValueError(f"Unknown browser name: {browser_name}")


class BaseHelpers:
    """Store base helpers of test framework"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)

    @log_action
    def is_element_exists(self, locator_type, locator):
        """Check if element exists; return Boolean"""
        try:
            self.wait_until_element_find(locator_type, locator)
        except TimeoutException:
            return False
        return True

    @log_action
    @wait_until_ok(timeout=5)
    def is_text_exists(self, locator_type, locator, text):
        """Check if text present; return Boolean"""
        try:
            self.wait_for_text(locator_type, locator, text)
            return True
        except TimeoutException:
            return False

    @log_action
    def is_checked(self, locator_type, locator):
        """Check if radio button is selected; return Boolean"""
        try:
            radio_button = self.wait_until_element_find(locator_type, locator)
            return radio_button.is_selected()
        except TimeoutException:
            return False

    @log_action
    def wait_until_element_find(self, locator_type, locator):
        """Wait until element is found and return it"""
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    @log_action
    def wait_until_elements_find(self, locator_type, locator):
        """Wait until elements are found and return them"""
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_elements(by=locator_type, value=locator)

    @log_action
    def wait_until_visible(self, locator_type, locator):
        self.wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    @log_action
    def wait_and_click(self, locator_type, locator):
        """Wait until element is clickable and click it"""
        self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator).click()

    @log_action
    def wait_for_text(self, locator_type, locator, text):
        """Wait until text appear on page"""
        self.wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))

    @log_action
    def fill_input_field(self, by, locator, value=""):
        """Find required element using by.X model, clear input field and enter the value"""
        field = self.wait_until_visible(locator_type=by, locator=locator)
        field.clear()
        field.send_keys(value)

    @log_action
    def find_by_contains_text(self, text, element_tag="*"):
        """Find element using XPATH contains function by text"""
        return self.wait_until_element_find(locator_type=By.XPATH,
                                            locator=f".//{element_tag}[contains(text(), '{text}')]")


class CustomerData:
    """Store customer data used for Log In and Register forms"""

    def __init__(self, gender="", first_name="", last_name="", email="", password=""):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


def random_customer():
    """Return namedtuple with random customer gender, first name, last name, email and password"""

    gender = random.choice(['male', 'female'])
    first_name = random.choice(Names.names[gender])
    last_name = random.choice(Names.names['last_name'])
    email = f"{first_name.lower()}.{last_name.lower()}@domain.com"
    password = f"{first_name}{random.randint(0, 10000)}"
    RandomCustomer = namedtuple('RandomCustomer', ['gender', 'first_name', 'last_name', 'email', 'password'])
    return RandomCustomer(gender, first_name, last_name, email, password)
