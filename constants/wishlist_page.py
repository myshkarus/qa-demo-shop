from .cart_page import CartPageConstants


class WishlistPageConstants:
    """Store constants related to the WishlistPage object"""

    LOCATOR_BY_TEXT = ".//*[contains(text(), '{text}')]"

    # Items in Wishlist
    TABLE_ROWS_ITEM_XPATH = CartPageConstants.TABLE_ROWS_ITEM_XPATH

    # Items details
    INPUT_CHECKBOX_REMOVE_ITEM_XPATH = CartPageConstants.INPUT_CHECKBOX_REMOVE_ITEM_XPATH
    INPUT_CHECKBOX_ADD_TO_CART_XPATH = ".//input[@name='addtocart']"
    LINK_PRODUCT_NAME_XPATH = ".//td[@class='product']/a"
    INPUT_FIELD_PRODUCT_QTY_XPATH = CartPageConstants.INPUT_FIELD_PRODUCT_QTY_XPATH
    PRODUCT_PRICE_XPATH = CartPageConstants.PRODUCT_PRICE_XPATH
    PRODUCT_SUBTOTAL_XPATH = CartPageConstants.PRODUCT_SUBTOTAL_XPATH

    # Buttons
    BUTTON_UPDATE_WISHLIST_XPATH = ".//input[@name='updatecart']"
    BUTTON_ADD_TO_CART_XPATH = ".//input[@name='addtocartbutton']"
    BUTTON_EMAIL_FRIEND_TEXT = "Email a friend'"
    BUTTON_EMAIL_FRIEND_XPATH = f".//input[@value='{BUTTON_EMAIL_FRIEND_TEXT}]"

    # Share wishlist link
    LINK_SHARE_WISHLIST_XPATH = ".//a[@class='share-link']"

    # Empty wishlist message
    MSG_WISHLIST_EMPTY_TEXT = "The wishlist is empty!"
