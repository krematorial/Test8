import pytest
from pages.search_page import SearchPage


@pytest.mark.parametrize("product_name, expected_result", [

    ("Book", True),

    ("NonExistentProduct", False),
])
def test_search(driver, product_name, expected_result):
    search_page = SearchPage(driver)
    search_page.driver.get("https://demowebshop.tricentis.com")
    search_page.search_for_product(product_name)

    if expected_result:
        assert product_name in search_page.get_product_titles()[0]
    else:
        assert "No products were found" in driver.page_source


