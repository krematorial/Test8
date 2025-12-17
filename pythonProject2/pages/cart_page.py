from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.login_page import LoginPage

class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "input.button-2.product-box-add-to-cart-button")
    CART_LINK = (By.LINK_TEXT, "Shopping cart")
    CART_ITEMS = (By.CLASS_NAME, "cart-item-row")
    QUANTITY_INPUT = (By.CLASS_NAME, "qty-input")
    UPDATE_CART_BUTTON = (By.NAME, "button-2.update-cart-button")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "bar-notification")
    UPDATE_CART_BUTTON = (By.NAME, "updatecart")

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def login_and_open_cart(self, email="validddd@example.com", password="Password123"):
        login_page = LoginPage(self.driver)
        login_page.driver.get("https://demowebshop.tricentis.com/login")
        login_page.login(email, password)

        # Переход в корзину после авторизации
        self.driver.get("https://demowebshop.tricentis.com/cart")

    def add_product_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

    def go_to_cart(self):
        self.wait_for_element(self.CART_LINK).click()
        self.wait_for_element(self.CART_ITEMS)

    def get_cart_items_count(self):
        self.wait_for_element(self.CART_ITEMS)
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def update_quantity(self, quantity):
        quantity_input = self.wait_for_element(self.QUANTITY_INPUT)
        quantity_input.clear()
        quantity_input.send_keys(quantity)

        self.wait_for_element(self.UPDATE_CART_BUTTON).click()

        if int(quantity) > 0:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element_value(self.QUANTITY_INPUT, str(quantity))
            )
        else:
            empty_cart_message = (By.CLASS_NAME, "order-summary-content")
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(empty_cart_message, "Your Shopping Cart is empty!")
            )

    def get_cart_empty_message(self):
        empty_cart_message = (By.CLASS_NAME, "order-summary-content")
        return self.wait_for_element(empty_cart_message).text.strip()


