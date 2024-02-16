from selenium import webdriver
from pages.StartPage import AuthPage
from pages.ProductsPage import ProductsPage
from pages.cart_page import CartPage
from pages.info_page import InfoPage
from pages.checkout_page import CheckoutPage



def test_labs_shopping():

    driver = webdriver.Chrome()
    auth = AuthPage(driver)
    auth.authorization()

    main = ProductsPage(driver)
    main.add_items_to_cart()
    main.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    info = InfoPage(driver)
    info.enter_your_details()

    checkout = CheckoutPage(driver)
    assert checkout.get_total() == ("Total: $58.29")

    driver.close()
