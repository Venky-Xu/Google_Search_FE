from behave import *
from selenium import webdriver
from pages.backoffice.bo_product_page import Products
from pages.marketplace.mp_onlinestore.mp_home_page import MPHomepage
from pages.marketplace.bo_marketplace.bo_getting_started.gettingstarted_page import GettingStarted
from pages.marketplace.mp_onlinestore.mp_product_details_page import ProductDetails
from pages.marketplace.mp_onlinestore.mp_checkout_step_one_page import CheckoutStepOne
from pages.marketplace.mp_onlinestore.mp_checkout_step_two_page import CheckoutStepTwo
from pages.marketplace.mp_onlinestore.mp_customer_login_signup_page import CustomerLogin
from pages.marketplace.mp_onlinestore.mp_payment_page import Payment
from pages.marketplace.mp_onlinestore.mp_order_confirmation_page import OrderConfirmation
import os


@given(u'Store is already online and published')
def step_impl(context):
    print("Make sure that store is online and published to continue executing this scenario")
    context.product = Products(context.driver)
    
@then(u'Add a product in BO')
def step_impl(context):
    context.product.add_product_with_variants_no_inventory() # product info

@step(u'Sell a product online and add to feature product list')
def step_impl(context):
    context.product_online_name = context.product.make_product_sell_online()

@then(u'Go to marketplace and verify if product is online or not')
def step_impl(context):
    context.online = GettingStarted(context.driver)
    context.online.launch_marketplace()
    context.mphome = MPHomepage(context.driver)
    context.mphome.verify_product_is_online_successfully(context.product_online_name)
    
@then(u'Click on product and verify product details like price, name and variants')
def step_impl(context):
    context.product_details = ProductDetails(context.driver)
    context.product_details.click_on_product_and_verify_details(context.product_online_name) # product_info
    
@step(u'Verify product stock status whether In stock or not')
def step_impl(context):
    context.product_details.verify_stock_status()
    
@then(u'Click on Add to cart')
def step_impl(context):
    context.product_details.add_product_to_cart()
    
@step(u'Verify product details in checkout pop and click on checkout')
def step_impl(context):
    context.product_details.click_on_checkout()
    
@then(u'Verify if user is directed to Checkout-Step 1 process')
def step_impl(context):
    context.checkout_step_one = CheckoutStepOne(context.driver)
    context.checkout_step_one.verify_checkout_step_one_direct_successfully()

@step(u'Click on Login and login using customer\'s login credentials')
def step_impl(context):
    context.customer_login = CustomerLogin(context.driver)
    context.customer_login.login_while_checkout(os.getenv("CUSTOMER_USERNAME"), os.getenv("CUSTOMER_PASSWORD"))

@then(u'Verify that user is logged in successfully and Contact Info should be autofilled.')
def step_impl(context):
    context.customer_login.verify_customer_login_successful_while_checkout()
    context.checkout_step_one.verify_contact_info_after_customer_login()

@step(u'Click on continue button to direct to Checkout-Step 2 process')
def step_impl(context):
    context.checkout_step_one.click_on_continue()
    
@then(u'Verify if successfully directed to checkout-step 2')
def step_impl(context):
    context.checkout_step_two = CheckoutStepTwo(context.driver)
    context.checkout_step_two.verify_checkout_step_two_direct_successfully()
    
@then(u'Select Delivery fulfillment method')
def step_impl(context):
    context.checkout_step_two.choose_fulfillment_method("Delivery")
    
@step(u'Add shipping address and click on save')
def step_impl(context):
    context.checkout_step_two.enter_shipping_address()


@then(u'Select shipping zone')
def step_impl(context):
    context.checkout_step_two.choose_shipping_zone()

@step(u'Verify if shipping fee is added to product price in Cart Summary')
def step_impl(context):
    context.delivery_fee = context.checkout_step_two.verify_delivery_fee_in_cart()


@then(u'Click on Proceed to pay for Delivery')
def step_impl(context):
    context.checkout_step_two.click_on_proceed_to_pay_delivery()
    context.checkout_step_two.check_for_error_message_while_proceeding_to_pay()
    

@step(u'Verify if it is directed to Payment page')
def step_impl(context):
    context.payment = Payment(context.driver)
    
    
@then(u'Enter all payment details and Proceed')
def step_impl(context):
    print("test")
    context.payment.click_on_proceed_to_pay_payment_page()


@then(u'Verify if payment is made and order is placed successfully')
def step_impl(context):
    context.order_confirmation = OrderConfirmation(context.driver)
    context.order_confirmation.verify_if_order_placed_successfully()


@step(u'Verify delivery order details in order confirmation page')
def step_impl(context):
    context.order_confirmation.verify_delivery_fee_in_order_summary(context.delivery_fee)

#----------Pick Up    
    
@then(u'Select Pickup fulfillment method')
def step_impl(context):
    context.checkout_step_two.choose_fulfillment_method("Pickup")
    

@step(u'Check availability of items in Pickup Store and select it')
def step_impl(context):
    context.checkout_step_two.check_availability_of_pickup_store()
    
    
@then(u'Click on Proceed to pay for Pickup')
def step_impl(context):
    context.checkout_step_two.click_on_proceed_to_pay_pickup()
    context.checkout_step_two.check_for_error_message_while_proceeding_to_pay()
    
@step(u'Verify pickup order details in order confirmation page')
def step_impl(context):
    print("test")
    
    
    