from .register_page import RegisterPageConstants
from .onepagecheckout_page import OnePageCheckoutPageConstants


class CustomerAccountPageConstants:
    """Store constants related to CustomerAccountPage object"""

    # Customer account side navigation panel
    LINK_CUSTOMER_INFO_XPATH = ".//div[@class='block block-account-navigation']//a[contains(text(), 'Customer info')]"
    LINK_ADDRESSES_XPATH = ".//div[@class='block block-account-navigation']//a[contains(text(), 'Addresses')]"
    LINK_ORDERS_XPATH = ".//div[@class='block block-account-navigation']//a[contains(text(), 'Orders')]"
    LINK_DOWNLOADABLE_PRODUCTS_XPATH = ".//div[@class='block block-account-navigation']//a[contains(text(), 'Downloadable products')]"
    LINK_BACK_IN_STOCK_SUBSCRIPTIONS_XPATH = ".//div[@class='block block-account-navigation']//a[contains(text(), 'Back in stock subscriptions')]"
    LINK_REWARD_POINTS_XPATH = ".//div[@class='block block-account-navigation']//a[contains(text(), 'Reward points')]"
    LINK_CHANGE_PASSWORD_XPATH = ".//div[@class='block block-account-navigation']//a[contains(text(), 'Change password')]"

    # Customer info
    INPUT_RADIO_GENDER_MALE_XPATH = RegisterPageConstants.INPUT_RADIO_GENDER_MALE_XPATH
    INPUT_RADIO_GENDER_FEMALE_XPATH = RegisterPageConstants.INPUT_RADIO_GENDER_FEMALE_XPATH
    INPUT_FIELD_FIRST_NAME_XPATH = RegisterPageConstants.INPUT_FIELD_FIRST_NAME_XPATH
    INPUT_FIELD_LAST_NAME_XPATH = RegisterPageConstants.INPUT_FIELD_LAST_NAME_XPATH
    INPUT_FIELD_EMAIL_XPATH = RegisterPageConstants.INPUT_FIELD_EMAIL_XPATH
    BUTTON_SAVE_XPATH = ".//input[@value='Save']"

    MSG_FIRST_NAME_REQUIRED_TEXT = OnePageCheckoutPageConstants.MSG_FIRST_NAME_REQUIRED_TEXT
    MSG_LAST_NAME_REQUIRED_TEXT = OnePageCheckoutPageConstants.MSG_LAST_NAME_REQUIRED_TEXT
    MSG_EMAIL_REQUIRED_TEXT = OnePageCheckoutPageConstants.MSG_EMAIL_REQUIRED_TEXT
