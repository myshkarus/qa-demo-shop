import logging
import os

import pytest

from constants.base import BaseConstants
from constants.login_page import LoginPageConstants
from helpers.base import random_customer, CustomerData
from pages.header_panel import HeaderPanel
from pages.home_page import HomePage


def pytest_sessionstart(session):
    """Pytest hook that runs before test session"""
    os.environ['PATH'] += os.pathsep + os.pathsep.join(
        [os.path.abspath(f'{BaseConstants.current_module}{os.path.sep}..{os.path.sep}drivers')])


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(item.name)


class BaseTest:
    log = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def home_page(driver):
    """Return Home Page"""
    driver.get(BaseConstants.START_PAGE_URL)
    return HomePage(driver)


@pytest.fixture(scope='function')
def login_page(home_page):
    """Open Login Page"""
    return home_page.header_panel.goto_login_page()


@pytest.fixture(scope='function')
def register_page(home_page):
    """Open Register Page"""
    return home_page.header_panel.goto_register_page()


@pytest.fixture(scope='function')
def logout(driver):
    """Log out the customer"""
    yield
    HeaderPanel(driver).logout_customer()


@pytest.fixture(scope='function')
def customer():
    """Get data of random customer"""
    new_customer = random_customer()
    return CustomerData(gender=new_customer.gender,
                        first_name=new_customer.first_name,
                        last_name=new_customer.last_name,
                        email=new_customer.email,
                        password=new_customer.password)


@pytest.fixture(scope='function')
def returning_customer():
    """Get data of returning customer"""
    returning: CustomerData = LoginPageConstants.registered
    return returning
