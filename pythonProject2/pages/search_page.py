from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-box-button")
    PRODUCT_TITLES = (By.CLASS_NAME, "product-title")

    def search_for_product(self, product_name):
        self.send_keys(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_product_titles(self):
        return [element.text for element in self.driver.find_elements(*self.PRODUCT_TITLES)]

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)