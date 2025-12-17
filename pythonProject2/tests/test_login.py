import pytest
import logging
from pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.mark.parametrize("email, password, expected_message", [
    ("validddd@example.com", "Password123", ""),
    ("invalid@example.com", "WrongPassword", "Login was unsuccessful."),

])
def test_login(driver, email, password, expected_message):
    logger.info(f"Starting test_login with email={email}, password={password}")
    login_page = LoginPage(driver)
    login_page.driver.get("https://demowebshop.tricentis.com/login")
    logger.info("Navigated to login page")
    login_page.login(email, password)
    logger.info("Login attempt completed")

    if expected_message:
        assert expected_message in login_page.get_error_message()
        logger.info("Error message verified")
    else:
        assert "Log out" in driver.page_source
        logger.info("Log out link found")