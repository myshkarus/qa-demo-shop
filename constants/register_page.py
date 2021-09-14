from .login_page import LoginPageConstants


class RegisterPageConstants:
    """Store constants related to the RegisterPage object"""

    # Register form
    INPUT_RADIO_GENDER_MALE_XPATH = ".//input[@id='gender-male']"
    INPUT_RADIO_GENDER_FEMALE_XPATH = ".//input[@id='gender-female']"
    INPUT_FIELD_FIRST_NAME_XPATH = ".//input[@id='FirstName']"
    INPUT_FIELD_LAST_NAME_XPATH = ".//input[@id='LastName']"
    INPUT_FIELD_EMAIL_XPATH = ".//input[@id='Email']"
    INPUT_FIELD_PASSWORD_XPATH = ".//input[@id='Password']"
    INPUT_FIELD_CONFIRM_PASSWORD_XPATH = ".//input[@id='ConfirmPassword']"
    BUTTON_REGISTER_XPATH = ".//input[@id='register-button']"

    # Successful registration
    SUCCESS_REGISTRATION_TEXT = "Your registration completed"
    BUTTON_CONTINUE_XPATH = ".//input[@value='Continue']"

    LOCATOR_BY_TEXT = LoginPageConstants.LOCATOR_BY_TEXT

    # Register form errors
    MSG_PASSWORD_AND_CONFIRMATION_PASSWORD_DO_NOT_MATCH_TEXT = "The password and confirmation password do not match."
    MSG_PASSWORD_REQUIRED_TEXT = "Password is required."
    MSG_PASSWORD_MIN_LENGTH_TEXT = "The password should have at least 6 characters."
    MSG_FIRST_NAME_REQUIRED_TEXT = "First name is required."
    MSG_LAST_NAME_REQUIRED_TEXT = "Last name is required."
    MSG_EMAIL_REQUIRED_TEXT = "Email is required."
    MSG_WRONG_EMAIL_TEXT = "Wrong email"
    MSG_ACCOUNT_ALREADY_EXISTS_TEXT = "The specified email already exists"
