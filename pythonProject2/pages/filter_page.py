from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class FilterPage(BasePage):
    FILTER_UNDER_25 = (By.XPATH, "//ul[@class='price-range-selector']//a[contains(text(), 'Under')]")
    FILTER_25_TO_50 = (By.XPATH, "//ul[@class='price-range-selector']//li//a//span[contains(text(), '25.00')]")
    FILTER_OVER_50 = (By.XPATH, "//ul[@class='price-range-selector']//a[contains(text(), 'Over')]")

    FILTERED_PRODUCTS = (By.CLASS_NAME, "product-item")

    def apply_price_filter(self, filter_option):
        """
        Применяет фильтр по цене, используя безопасный клик.
        :param filter_option: Один из фильтров (FILTER_UNDER_25, FILTER_25_TO_50, FILTER_OVER_50).
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(filter_option)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(filter_option)
        )
        self.driver.execute_script("arguments[0].click();", element)  # Клик через JS

    def get_filtered_products_count(self):
        return len(self.driver.find_elements(*self.FILTERED_PRODUCTS))

    def apply_nonexistent_filter(self):

        NONEXISTENT_FILTER = (By.XPATH, "//a[contains(text(), 'Nonexistent Filter')]")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(NONEXISTENT_FILTER)
            ).click()
        except Exception as e:
            print(f"Nonexistent filter not found: {e}")
