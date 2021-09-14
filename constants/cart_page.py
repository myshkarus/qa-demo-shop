class CartPageConstants:
    """Store constants related to the CartPage object"""

    # Empty cart
    MSG_EMPTY_CART_TEXT = "Your Shopping Cart is empty!"
    MSG_EMPTY_CART_XPATH = ".//div[@class='order-summary-content']"

    # Items in cart
    TABLE_ROWS_ITEM_XPATH = ".//table[@class='cart']//tr[@class='cart-item-row']"

    # Items details
    INPUT_CHECKBOX_REMOVE_ITEM_XPATH = ".//input[@name='removefromcart']"
    LINK_PRODUCT_NAME_XPATH = ".//a[@class='product-name']"
    INPUT_FIELD_PRODUCT_QTY_XPATH = ".//input[@class='qty-input']"
    PRODUCT_PRICE_XPATH = ".//span[@class='product-unit-price']"
    PRODUCT_SUBTOTAL_XPATH = ".//span[@class='product-subtotal']"

    # Buttons
    BUTTON_UPDATE_CART_XPATH = ".//input[@name='updatecart']"
    BUTTON_CONTINUE_SHOPPING_XPATH = ".//input[@name='continueshopping']"

    # Discount & gift
    INPUT_FIELD_DISCOUNT_COUPON_CODE_XPATH = ".//input[@name='discountcouponcode']"
    BUTTON_APPLY_DISCOUNT_COUPON_CODE_XPATH = ".//input[@name='applydiscountcouponcode']"
    INPUT_FIELD_GIFT_COUPON_CODE_XPATH = ".//input[@name='giftcardcouponcode']"
    BUTTON_ADD_GIFT_CART_XPATH = ".//input[@name='applygiftcardcouponcode']"

    # Messages
    MSG_WRONG_COUPON_CODE_TEXT = "The coupon code you entered couldn't be applied to your order"
    MSG_WRONG_COUPON_CODE_XPATH = f'.//div[@class="message" and contains(text(), \"{MSG_WRONG_COUPON_CODE_TEXT}\")]'

    # Estimate shipping
    SELECT_COUNTRY_ID_XPATH = ".//select[@id='CountryId']"
    SELECT_STATE_PROVINCE_ID_XPATH = ".//select[@id='StateProvinceId']"
    INPUT_FIELD_ZIP_POSTAL_CODE_XPATH = ".//input[@id='ZipPostalCode']"
    INPUT_FIELD_ESTIMATE_SHIPPING_XPATH = ".//input[@name='estimateshipping']"

    # Cart's total
    CART_SUB_TOTALS_VALUE_XPATH = ".//table[@class='cart-total']//span[contains(text(), 'Sub-Total:')]/../..//span[@class='product-price']"
    CART_SHIPPING_VALUE_XPATH = ".//table[@class='cart-total']//span[contains(text(), 'Shipping:')]/../..//span/span"
    CART_TAX_VALUE_XPATH = ".//table[@class='cart-total']//span[contains(text(), 'Tax:')]/../..//span[@class='product-price']"
    CART_TOTAL_VALUE_XPATH = ".//table[@class='cart-total']//span[contains(text(), ' Total:')]/../..//span/span"

    # Checkout
    BUTTON_CHECKOUT_XPATH = ".//button[@id='checkout']"

    # Auxiliary
    INPUT_CHECKBOX_TERMS_XPATH = ".//input[@id='termsofservice']"
