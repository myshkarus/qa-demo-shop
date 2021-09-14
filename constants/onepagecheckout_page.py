from .cart_page import CartPageConstants


class OnePageCheckoutPageConstants:
    """Store constants related to the CheckoutPage object"""

    # Billing address errors
    MSG_FIRST_NAME_REQUIRED_TEXT = "First name is required."
    MSG_LAST_NAME_REQUIRED_TEXT = "Last name is required."
    MSG_EMAIL_REQUIRED_TEXT = "Email is required."
    MSG_WRONG_EMAIL_TEXT = "Wrong email"
    MSG_COUNTRY_REQUIRED_TEXT = "Country is required."
    MSG_CITY_REQUIRED_TEXT = "City is required"
    MSG_STREET_REQUIRED_TEXT = "Street address is required"
    MSG_ZIP_POSTAL_CODE_REQUIRED_TEXT = "Zip / postal code is required"
    MSG_PHONE_REQUIRED_TEXT = "Phone is required"

    # Billing address fields
    INPUT_FIELD_REQUIRED_FIRST_NAME_XPATH = ".//input[@id='BillingNewAddress_FirstName']"
    INPUT_FIELD_REQUIRED_LAST_NAME_XPATH = ".//input[@id='BillingNewAddress_LastName']"
    INPUT_FIELD_REQUIRED_EMAIL_XPATH = ".//input[@id='BillingNewAddress_Email']"
    INPUT_FIELD_COMPANY_XPATH = ".//input[@id='BillingNewAddress_Company']"
    INPUT_FIELD_REQUIRED_COUNTRY_ID_XPATH = ".//select[@id='BillingNewAddress_CountryId']"
    INPUT_FIELD_STATE_PROVINCE_ID_XPATH = ".//select[@id='BillingNewAddress_StateProvinceId']"
    INPUT_FIELD_REQUIRED_CITY_XPATH = ".//input[@id='BillingNewAddress_City']"
    INPUT_FIELD_REQUIRED_ADDRESS1_XPATH = ".//input[@id='BillingNewAddress_Address1']"
    INPUT_FIELD_ADDRESS2_XPATH = ".//input[@id='BillingNewAddress_Address2']"
    INPUT_FIELD_REQUIRED_ZIP_POSTAL_CODE_XPATH = ".//input[@id='BillingNewAddress_ZipPostalCode']"
    INPUT_FIELD_REQUIRED_PHONE_NUMBER_XPATH = ".//input[@id='BillingNewAddress_PhoneNumber']"
    INPUT_FIELD_FAX_NUMBER_XPATH = ".//input[@id='BillingNewAddress_FaxNumber']"

    BUTTON_BILLING_ADDRESS_CONTINUE_XPATH = ".//div[@id='billing-buttons-container']/input[@title='Continue']"

    # Shipping address
    SELECT_SHIPPING_ADDRESS_XPATH = ".//select[@id='shipping-address-select']"
    INPUT_CHECKBOX_IN_STORE_PICKUP_XPATH = ".//input[@id='PickUpInStore']"
    LINK_BACK_TO_BILLING_ADDRESS_XPATH = ".//div[@id='shipping-buttons-container']/*/a[contains(text(), 'Back')]"
    BUTTON_SHIPPING_ADDRESS_CONTINUE_XPATH = ".//div[@id='shipping-buttons-container']/input[@title='Continue']"

    # Shipping method
    INPUT_RADIO_GROUND_METHOD_XPATH = ".//div[@class='method-name']/label[contains(text(), 'Ground')]/../input"
    INPUT_RADIO_NEXT_DAY_METHOD_XPATH = ".//div[@class='method-name']/label[contains(text(), 'Next Day Air')]/../input"
    INPUT_RADIO_SECOND_DAY_METHOD_XPATH = ".//div[@class='method-name']/label[contains(text(), '2nd Day Air')]/../input"
    LINK_BACK_TO_SHIPPING_ADDRESS_XPATH = ".//div[@id='shipping-method-buttons-container']/*/a[contains(text(), 'Back')]"
    BUTTON_SHIPPING_METHOD_CONTINUE_XPATH = ".//div[@id='shipping-method-buttons-container']/input[@value='Continue']"

    # Payment method
    INPUT_RADIO_CASH_ON_DELIVERY_METHOD_XPATH = ".//div[@class='method-name']//label[contains(text(), 'Cash On Delivery')]/../input"
    INPUT_RADIO_CHECK_MONEY_ORDER_METHOD_XPATH = ".//div[@class='method-name']//label[contains(text(), 'Check / Money Order')]/../input"
    INPUT_RADIO_CREDIT_CARD_METHOD_XPATH = ".//div[@class='method-name']//label[contains(text(), 'Credit Card')]/../input"
    INPUT_RADIO_PURCHASE_ORDER_METHOD_XPATH = ".//div[@class='method-name']//label[contains(text(), 'Purchase Order')]/../input"
    LINK_BACK_TO_SHIPPING_METHOD_XPATH = ".//div[@id='payment-method-buttons-container']/*/a[contains(text(), 'Back')]"
    BUTTON_PAYMENT_METHOD_CONTINUE_XPATH = ".//div[@id='payment-method-buttons-container']/input[@value='Continue']"

    # Payment info
    LINK_BACK_TO_PAYMENT_METHOD_XPATH = ".//div[@id='payment-info-buttons-container']/*/a[contains(text(), 'Back')]"
    BUTTON_PAYMENT_INFO_CONTINUE_XPATH = ".//div[@id='payment-info-buttons-container']/input[@value='Continue']"

    # Confirm order
    CART_SUB_TOTALS_VALUE_XPATH = CartPageConstants.CART_SUB_TOTALS_VALUE_XPATH
    CART_SHIPPING_VALUE_XPATH = CartPageConstants.CART_SHIPPING_VALUE_XPATH
    CART_PAYMENT_METHOD_ADDITIONAL_FEE = ".//table[@class='cart-total']//span[contains(text(), 'Payment method additional fee:')]/../..//span/span"
    CART_TAX_VALUE_XPATH = CartPageConstants.CART_TAX_VALUE_XPATH
    CART_TOTAL_VALUE_XPATH = CartPageConstants.CART_TOTAL_VALUE_XPATH

    LINK_PRODUCT_NAME_XPATH = CartPageConstants.LINK_PRODUCT_NAME_XPATH
    PRODUCT_UNIT_PRICE_XPATH = CartPageConstants.PRODUCT_PRICE_XPATH
    PRODUCT_QTY_XPATH = ".//td[@class='qty nobr']/span[not(@class)]"
    PRODUCT_SUBTOTAL_XPATH = CartPageConstants.PRODUCT_SUBTOTAL_XPATH

    LINK_BACK_TO_PAYMENT_INFO_XPATH = ".//div[@id='confirm-order-buttons-container']/*/a[contains(text(), 'Back')]"
    BUTTON_CONFIRM_ORDER_XPATH = ".//div[@id='confirm-order-buttons-container']/input[@value='Confirm']"
