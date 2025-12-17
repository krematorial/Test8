from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CHECKOUT_BUTTON = (By.NAME, "checkout")
    BILLING_ADDRESS_FORM = (By.ID, "billing-address-select")
    PAYMENT_METHOD = (By.ID, "paymentmethod_1")
    CONFIRM_ORDER_BUTTON = (By.CLASS_NAME, "confirm-order-next-step-button")
    ORDER_SUCCESS_MESSAGE = (By.CLASS_NAME, "order-completed")

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def select_billing_address(self):
        self.click(self.BILLING_ADDRESS_FORM)

    def select_payment_method(self):
        self.click(self.PAYMENT_METHOD)

    def confirm_order(self):
        self.click(self.CONFIRM_ORDER_BUTTON)

    def get_order_success_message(self):
        return self.get_text(self.ORDER_SUCCESS_MESSAGE)