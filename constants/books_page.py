from constants.login_page import LoginPageConstants


class BooksPageConstants:
    """Store constants related to the BooksPage object"""

    # Wishlisted Items (for testing)
    BOOK_PRODUCT_FICTION_TEXT = "Fiction EX"
    BOOK_PRODUCT_HEALTH_TEXT = "Health Book"

    # Filters
    SELECT_PRODUCTS_ORDERBY_XPATH = ".//select[@id='products-orderby']"
    SELECT_PRODUCTS_PAGESIZE_XPATH = ".//select[@id='products-pagesize']"
    SELECT_PRODUCTS_VIEWMODE_XPATH = ".//select[@id='products-viewmode']"
    LINK_PRICE_RANGE_SELECTOR_XPATH = ".//ul[@class='price-range-selector']//a"

    # Product item
    LIST_OF_PRODUCTS_XPATH = ".//div[@class='details']"
    PRODUCT_TITLE_XPATH = ".//h2[@class='product-title']"
    PRICE_OLD_XPATH = ".//span[@class='price old-price']"
    PRICE_ACTUAL_XPATH = ".//span[@class='price actual-price']"
    BUTTON_ADD_TO_CART_XPATH = ".//input[@value='Add to cart']"

    # Page navigation
    CURRENT_PAGE_XPATH = ".//li[@class='current-page']/span"
    INDIVIDUAL_PAGE_XPATH = ".//li[@class='individual-page']/a"
    NEXT_PAGE_XPATH = ".//li[@class='next-page']/a"

    BUTTON_ADD_TO_WISHLIST_XPATH = ".//div[@class='add-to-cart-panel']/input[@value='Add to wishlist']"
    LOCATOR_BY_TEXT = LoginPageConstants.LOCATOR_BY_TEXT
