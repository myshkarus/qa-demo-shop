class HeaderPanelConstants:
    """Store constants related to HeaderPanel object"""

    # Go to store pages
    LINK_REGISTER_XPATH = ".//a[@href='/register']"
    LINK_LOGIN_XPATH = ".//a[@href='/login']"
    LINK_CART_XPATH = ".//div[@class='header-links']//a[@href='/cart']"
    LINK_WISHLIST_XPATH = ".//div[@class='header-links']//a[@href='/wishlist']"
    LINK_LOGOUT_XPATH = ".//a[@href='/logout']"

    # Logged in customer
    LINK_LOGGED_IN_CUSTOMER_XPATH = ".//a[contains(text(), '{email_lower}')]"

    # Search store
    INPUT_FIELD_SEARCH_XPATH = ".//input[@id='small-searchterms']"
    BUTTON_SEARCH_XPATH = ".//input[@type='submit']"

    # Return to Home Page
    LINK_HOME_PAGE_XPATH = ".//a[@href='/']"

