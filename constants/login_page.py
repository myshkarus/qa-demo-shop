from helpers.base import CustomerData


class LoginPageConstants:
    """Store constants related to the LoginPage object"""

    LOCATOR_BY_TEXT = ".//*[contains(text(), '{text}')]"

    # Login form
    INPUT_FIELD_EMAIL_XPATH = ".//input[@id='Email']"
    INPUT_FIELD_PASSWORD_XPATH = ".//input[@id='Password']"
    INPUT_CHECKBOX_REMEMBER_ME_XPATH = ".//input[@id='RememberMe']"
    LINK_PASSWORD_RECOVERY_XPATH = ".//a[@href='/passwordrecovery']"
    BUTTON_REGISTER_XPATH = ".//input[@type='button' and @value='Register']"
    BUTTON_CHECKOUT_AS_GUEST_XPATH = ".//input[@type='button' and @value='Checkout as Guest']"
    BUTTON_LOGIN_XPATH = ".//input[@type='submit' and @value='Log in']"

    # Unsuccessful login
    MSG_UNSUCCESSFUL_LOGIN_TEXT = "Login was unsuccessful. Please correct the errors and try again."

    # Wrong account
    MSG_NO_CUSTOMER_ACCOUNT_FOUND_TEXT = "No customer account found"

    # Incorrect email
    MSG_INCORRECT_EMAIL_TEXT = "Please enter a valid email address."

    # Wrong password
    MSG_INCORRECT_CREDENTIALS_TEXT = "The credentials provided are incorrect"

    # Data of imaginary customer
    REGISTERED_CUSTOMER_EMAIL = 'anna.smith@domain.com'
    _REGISTERED_CUSTOMER_GENDER = 'female'
    _REGISTERED_CUSTOMER_FIRST_NAME = 'Anna'
    _REGISTERED_CUSTOMER_LAST_NAME = 'Smith'
    _REGISTERED_CUSTOMER_PASSWORD = '1234567'

    registered = CustomerData(gender=_REGISTERED_CUSTOMER_GENDER,
                              first_name=_REGISTERED_CUSTOMER_FIRST_NAME,
                              last_name=_REGISTERED_CUSTOMER_LAST_NAME,
                              email=REGISTERED_CUSTOMER_EMAIL,
                              password=_REGISTERED_CUSTOMER_PASSWORD)
