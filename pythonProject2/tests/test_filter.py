import pytest
import logging
from pages.filter_page import FilterPage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_filter(driver):
    logger.info("Starting test_filter")
    filter_page = FilterPage(driver)
    filter_page.driver.get("https://demowebshop.tricentis.com/books")
    logger.info("Navigated to books page")

    filter_page.apply_price_filter(filter_page.FILTER_UNDER_25)
    logger.info("Applied 'Under $25' filter")

    filtered_products_count = filter_page.get_filtered_products_count()
    logger.info(f"Found {filtered_products_count} products after applying filter")
    assert filtered_products_count > 0, "No products found after applying filter"

    logger.info("Test completed")

def test_nonexistent_filter(driver):
    logger.info("Starting test_nonexistent_filter")
    filter_page = FilterPage(driver)
    filter_page.driver.get("https://demowebshop.tricentis.com/books")
    logger.info("Navigated to books page")

    initial_count = filter_page.get_filtered_products_count()
    logger.info(f"Initial product count: {initial_count}")

    filter_page.apply_nonexistent_filter()
    logger.info("Attempted to apply nonexistent filter")

    current_count = filter_page.get_filtered_products_count()
    logger.info(f"Current product count: {current_count}")
    assert current_count == initial_count, "Product count changed after applying nonexistent filter"

    logger.info("Test completed")