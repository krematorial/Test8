from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPage(BasePage):
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".ico-register")
    FIRST_NAME_INPUT = (By.ID, "FirstName")
    LAST_NAME_INPUT = (By.ID, "LastName")
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "ConfirmPassword")
    REGISTER_SUBMIT_BUTTON = (By.ID, "register-button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".result")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".field-validation-error")

    def open_registration_page(self):
        self.click(self.REGISTER_BUTTON)
    def register_user(self, first_name, last_name, email, password):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.EMAIL_INPUT, email)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, password)
        self.click(self.REGISTER_SUBMIT_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        errors = self.driver.find_elements(*self.ERROR_MESSAGE)
        if errors:
            return errors[0].text
        return ""