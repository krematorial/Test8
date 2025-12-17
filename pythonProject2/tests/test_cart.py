import pytest
from pages.cart_page import CartPage

def test_add_to_cart(driver):
    cart_page = CartPage(driver)

    # Авторизация перед тестом и переход в корзину
    cart_page.login_and_open_cart()

    cart_page.driver.get("https://demowebshop.tricentis.com/books")
    cart_page.add_product_to_cart()
    cart_page.go_to_cart()

    assert cart_page.get_cart_items_count() == 1


def test_edit_cart(driver):
    cart_page = CartPage(driver)

    # Авторизация перед тестом и переход в корзину
    cart_page.login_and_open_cart()

    cart_page.driver.get("https://demowebshop.tricentis.com/books")
    cart_page.add_product_to_cart()
    cart_page.go_to_cart()
    cart_page.update_quantity("2")

    assert cart_page.get_cart_items_count() == 1


def test_edit_cart_with_invalid_quantity(driver): #Отрицательный тест
    cart_page = CartPage(driver)

    cart_page.login_and_open_cart()

    cart_page.driver.get("https://demowebshop.tricentis.com/books")
    cart_page.add_product_to_cart()
    cart_page.go_to_cart()

    cart_page.update_quantity("-1")

    assert "Your Shopping Cart is empty!" in cart_page.get_cart_empty_message()
