from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart-button")
    PRODUCT_NAME = (By.CLASS_NAME, "product-name")

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)