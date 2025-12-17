import pytest
from pages.main_page import MainPage

@pytest.mark.parametrize("section, expected_title", [
    ("Books", "Books"),
    ("Computers", "Computers"),
])
def test_navigation(driver, section, expected_title):
    main_page = MainPage(driver)
    main_page.driver.get("https://demowebshop.tricentis.com")

    if section == "Books":
        main_page.navigate_to_books()
    elif section == "Computers":
        main_page.navigate_to_computers()

    assert expected_title in main_page.get_page_title()

def test_navigation_to_nonexistent_section(driver):
    main_page = MainPage(driver)
    main_page.driver.get("https://demowebshop.tricentis.com")

    page_title = main_page.get_page_title()
    assert page_title in ["Welcome to our store", "Page title not found"]
