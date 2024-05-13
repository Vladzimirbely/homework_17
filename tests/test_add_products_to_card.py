import allure
from selene import browser, have
from allure import attach
from allure_commons.types import AttachmentType
import requests

class Cart:
    def open_to_cart(self):
        with allure.step('Open cart'):
            browser.open('/cart')
            return self

    @staticmethod
    def open_cart_with_products(url=None, data=None):
        with allure.step('Open cart with products'):
            result = requests.post(url=url, data=data)
            cookies = result.cookies.get('Nop.customer')
            attach(body=cookies, name='cookies', attachment_type=AttachmentType.TEXT)
            browser.open('https://demowebshop.tricentis.com/cart')
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookies})

add_products_to_cart = Cart()
page_of_product = 'https://demowebshop.tricentis.com/addproducttocart/catalog'

def test_add_book_to_cart():
    with allure.step('Add book to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/13/1/1')
    browser.open('/')
    with allure.step('Open cart with book'):
        add_products_to_cart.open_to_cart()

    assert browser.element('.product-name').should(have.text('Computing and Internet'))
    assert browser.element('.product-subtotal').should(have.text('10.00'))
    assert browser.element('.product-unit-price').should(have.text('10.00'))


def test_add_laptop_to_cart():
    with allure.step('Add laptop to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/31/1/1')
    browser.open('/')
    with allure.step('Open cart with laptop'):
        add_products_to_cart.open_to_cart()

    assert browser.element('.product-name').should(have.text('14.1-inch Laptop'))
    assert browser.element('.product-subtotal').should(have.text('1590.00'))
    assert browser.element('.product-unit-price').should(have.text('1590.00'))


def test_add_jeans_to_cart():
    with allure.step('Add jeans to cart'):
        add_products_to_cart.open_cart_with_products(
            url=f'{page_of_product}/36/1/1')
    browser.open('/')
    with allure.step('Open cart with jeans'):
        add_products_to_cart.open_to_cart()

    assert browser.element('.product-name').should(have.text('Blue Jeans'))
    assert browser.element('.product-subtotal').should(have.text('1.00'))
    assert browser.element('.product-unit-price').should(have.text('1.00'))
