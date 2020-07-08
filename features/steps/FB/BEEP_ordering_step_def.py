from behave import *
from features.pages.beep.BEEP_stores_page import Stores
from features.pages.beep.BEEP_order_page import Order
from features.pages.beep.BEEP_select_payment_page import PaymentSelection
from features.pages.beep.BEEP_pay_via_card_page import Card
from features.pages.beep.BEEP_2c2p_page import Payment
from features.pages.beep.BEEP_order_paid_page import Paid
from decimal import Decimal
import time



@given(u'Navigate to a store')
def step_impl(context):
    context.store = Stores(context.chrome_driver)
    context.store.choose_store()


@when(u'Add an item to cart and checkout')
def step_impl(context):
    context.order = Order(context.chrome_driver)
    item_info = context.order.add_item_into_cart()
    context.subtotal = Decimal(item_info['single_price']) * int(item_info['quantity'])
    context.order.verify_items_in_cart(int(item_info['quantity']))
    total_info = context.order.checkout_and_pay()
    assert Decimal(total_info['subtotal']) == context.subtotal
    context.total = total_info['total']


@then(u'payment')
def step_impl(context):
    context.select = PaymentSelection(context.chrome_driver)
    context.select.pay_now()
    context.card = Card(context.chrome_driver)
    time.sleep(2)
    context.card.card_information_input(5555555555554444, 1234, 123, 'test')
    context.chrome_driver.implicitly_wait(10)
    context.chrome_driver.implicitly_wait(20)
    context.payment = Payment(context.chrome_driver)
    context.payment.input_opt_and_continue(123456)
    context.chrome_driver.implicitly_wait(10)
    context.paid = Paid(context.chrome_driver)
    context.paid.transfer_to_order_paid()

