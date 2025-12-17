import pytest
import time
from pages.registration_page import RegistrationPage

def generate_unique_email():
    return f"john.doe{int(time.time())}@example.com"

@pytest.mark.parametrize("first_name, last_name, password, expected_message", [
    ("John", "Doe", "Password123", "Your registration completed"),
    ("John", "", "Password123", "Last name is required."),])
def test_registration(driver, first_name, last_name, password, expected_message):
    registration_page = RegistrationPage(driver)
    registration_page.driver.get("https://demowebshop.tricentis.com")
    registration_page.open_registration_page()
    email = generate_unique_email()
    registration_page.register_user(first_name, last_name, email, password)

    if "required" in expected_message or "Wrong" in expected_message or "should have" in expected_message:
        assert expected_message in registration_page.get_error_message()
    else:
        assert expected_message in registration_page.get_success_message()