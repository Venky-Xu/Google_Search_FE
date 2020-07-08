from behave import *
from features.pages.beep.BEEP_stores_page import Stores
from features.pages.beep.BEEP_preference_selection_page import Preference
from features.pages.beep.BEEP_order_page import Order
from features.pages.beep.BEEP_select_payment_page import PaymentSelection
from features.pages.beep.BEEP_pickup_details_page import Details as Pickup_Details
from features.pages.beep.BEEP_delivery_detail_page import Details as Deliver_Details
from features.pages.beep.BEEP_pay_via_card_page import Card
from features.pages.beep.BEEP_2c2p_page import Payment
from features.pages.beep.BEEP_order_paid_page import Paid
from features.pages.beep.BEEP_scan_page import Scan
from features.pages.beep.BEEP_deliver_to_page import Deliver
from features.pages.beep.BEEP_preorder_pickup_page import PrePickup
from features.pages.beep.BEEP_pay_via_online_banking import Online
from features.pages.beep.BEEP_stripe import Stripe
from util.util import Util
from util.commonfunctions import Actions
import time
from decimal import Decimal


def intermediate_process(context):
    context.order = Order(context.chrome_driver)
    context.order.legal_drinking_age()
    time.sleep(1)
    context.order.clear_shopping_cart()
    context.chrome_driver.implicitly_wait(10)
    item_info = context.order.add_item_into_cart()
    context.subtotal = Decimal(item_info['single_price']) * int(item_info['quantity'])
    time.sleep(1)
    context.order.verify_items_in_cart(int(item_info['quantity']))
    total_info = context.order.checkout_and_pay()
    assert Decimal(total_info['subtotal']) == context.subtotal
    context.total = total_info['total']


def intermediate_process_mvp(context):
    context.order = Order(context.chrome_driver)
    Actions(context.chrome_driver).add_cookies()
    context.order.legal_drinking_age()
    time.sleep(2)
    context.order.clear_shopping_cart()
    item_info = context.order.add_item_into_cart()
    context.subtotal = Decimal(item_info['single_price']) * int(item_info['quantity'])
    context.order.verify_items_in_cart(int(item_info['quantity']))
    context.order.checkout()
    context.pre = PrePickup(context.chrome_driver)
    context.pre.choose_pickup_date()
    context.order.pay()


def intermediate_process_pre(context):
    context.order = Order(context.chrome_driver)
    context.order.legal_drinking_age()
    time.sleep(2)
    context.order.clear_shopping_cart()
    item_info = context.order.add_item_into_cart()
    context.subtotal = Decimal(item_info['single_price']) * int(item_info['quantity'])
    context.order.verify_items_in_cart(int(item_info['quantity']))
    total_info = context.order.checkout_and_pay()
    assert Decimal(total_info['subtotal']) == context.subtotal
    context.total = total_info['total']
    context.pre = PrePickup(context.chrome_driver)
    context.pre.choose_pickup_date()
    total_info = context.order.pay()
    assert Decimal(total_info['subtotal']) == context.subtotal
    context.total = total_info['total']


def intermediate_process_safari(context):
    context.order = Order(context.safari_driver)
    context.order.clear_shopping_cart_safari()
    item_info = context.order.add_item_into_cart_safari()
    context.subtotal = Decimal(item_info['single_price']) * int(item_info['quantity'])
    context.order.verify_items_in_cart(int(item_info['quantity']))
    total_info = context.order.checkout_and_pay_safari()
    assert Decimal(total_info['subtotal']) == context.subtotal
    context.total = total_info['total']


@given(u'Navigate to a store and choose Self pickup')
def step_impl(context):
    time.sleep(2)
    Actions(context.chrome_driver).navigate_to_url(Util.BEEP_DELIVERY_URL)
    Actions(context.chrome_driver).add_cookies()
    context.store = Stores(context.chrome_driver)
    context.chrome_driver.implicitly_wait(10)
    context.store.choose_store()
    context.chrome_driver.implicitly_wait(10)
    time.sleep(2)
    context.preference = Preference(context.chrome_driver)
    context.preference.select_preference_pickup()
    context.pre = PrePickup(context.chrome_driver)
    context.pre.choose_pickup_date()
    context.chrome_driver.implicitly_wait(10)


@given(u'Navigate to a store and choose Food delivery')
def step_impl(context):
    Actions(context.chrome_driver).navigate_to_url(Util.BEEP_DELIVERY_URL)
    Actions(context.chrome_driver).add_cookies()

    context.store = Stores(context.chrome_driver)
    context.chrome_driver.implicitly_wait(10)
    context.store.choose_store()
    context.chrome_driver.implicitly_wait(10)
    time.sleep(2)
    context.preference = Preference(context.chrome_driver)
    context.preference.select_preference_delivery()
    context.pre = PrePickup(context.chrome_driver)
    context.pre.choose_delivery_date()
    context.pre.click_deliver_to()
    context.deliver = Deliver(context.chrome_driver)
    context.deliver.select_address()
    context.chrome_driver.implicitly_wait(10)
    context.pre.continue_click()


@given(u'Navigate to a store which without preorder and choose Food delivery')
def step_impl(context):
    context.chrome_driver.get(Util.MVP_BEEP_DELIVERY_URL)
    context.chrome_driver.implicitly_wait(10)
    context.store = Stores(context.chrome_driver)
    context.chrome_driver.implicitly_wait(10)
    context.store.choose_store()
    context.chrome_driver.implicitly_wait(10)
    time.sleep(2)
    context.preference = Preference(context.chrome_driver)
    context.preference.select_preference_delivery()


@when(u'Add an item into cart and fill pickup information')
def step_impl(context):
    context.chrome_driver.implicitly_wait(20)
    intermediate_process(context)
    context.pickup_detail = Pickup_Details(context.chrome_driver)
    context.pickup_detail.input_name_and_phone_number('test', '+8615995375101')


@when(u'Select delivery to address and add an item into cart')
def step_impl(context):
    intermediate_process(context)
    context.deliver_details = Deliver_Details(context.chrome_driver)
    context.deliver_details.input_delivery_info('test', '+8615995375101')


@then(u'payment process')
def step_impl(context):
    context.select = PaymentSelection(context.chrome_driver)
    context.select.pay_now()
    context.chrome_driver.implicitly_wait(10)
    context.online = Online(context.chrome_driver)
    context.online.choose_bank_and_pay()
    context.chrome_driver.implicitly_wait(10)
    context.stripe = Stripe(context.chrome_driver)
    context.stripe.authorize_test_payment()
    context.chrome_driver.implicitly_wait(10)
    context.paid = Paid(context.chrome_driver)
    context.order_id = context.paid.transfer_to_order_paid()


@given(u'Navigate to scan homepage')
def step_impl(context):
    Actions(context.chrome_driver).navigate_to_url(Util.MVP_BEEP_DELIVERY_URL)
    Actions(context.chrome_driver).set_local_storage('user.placeInfo', '{"coords":{"lat":3.1580207,"lng":101.7116671},"address":"KLCC, Kuala Lumpur City Centre, Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia","addressComponents":{"street1":"","street2":"Kuala Lumpur City Centre","city":"Kuala Lumpur","state":"Wilayah Persekutuan Kuala Lumpur","country":"Malaysia","countryCode":"MY"},"placeId":"ChIJH5xmLdE3zDERKa4a_IywVck","displayComponents":{"mainText":"KLCC","secondaryText":"Kuala Lumpur City Centre, Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia"}}')
    time.sleep(2)
    Actions(context.chrome_driver).navigate_to_url(Util.MVP_BEEP_DELIVERY_URL)
    context.scan = Scan(context.chrome_driver)
    Actions(context.chrome_driver).add_cookies()


@step(u'Select delivery to location and store')
def step_impl(context):
    context.scan = Scan(context.chrome_driver)
    context.scan.change_deliver_to_location()
    context.chrome_driver.implicitly_wait(10)
    context.deliver = Deliver(context.chrome_driver)
    context.deliver.select_address()
    context.chrome_driver.implicitly_wait(10)
    context.scan.select_store('Auto For Beep Delivery')
    context.chrome_driver.implicitly_wait(10)


@step(u'Select delivery to location and self pickup store')
def step_impl(context):
    context.scan = Scan(context.chrome_driver)
    context.scan.change_deliver_to_location()
    context.chrome_driver.implicitly_wait(10)
    context.deliver = Deliver(context.chrome_driver)
    context.deliver.select_address()
    context.chrome_driver.implicitly_wait(10)
    context.scan.select_self_pickup_store()
    context.chrome_driver.implicitly_wait(10)


@step(u'Select delivery to location and store which without preorder, choose Food delivery')
def step_impl(context):
    context.deliver = Deliver(context.chrome_driver)
    context.deliver.select_address()
    context.chrome_driver.implicitly_wait(10)
    context.scan.select_store('AutoforBeepDeliverySpare')
    time.sleep(2)
    context.scan.choose_food_delivery()


@step(u'Select delivery to location and store, choose Self pickup')
def step_impl(context):
    context.deliver = Deliver(context.chrome_driver)
    context.deliver.select_address()
    context.chrome_driver.implicitly_wait(10)
    context.scan.select_store('Auto For Beep Delivery')
    time.sleep(2)
    context.scan.choose_self_pickup()


@step(u'Select delivery to location and store which without preorder, choose Self pickup')
def step_impl(context):
    context.deliver = Deliver(context.chrome_driver)
    context.deliver.select_address()
    context.chrome_driver.implicitly_wait(10)
    context.scan.select_store('AutoforBeepDeliverySpare')
    time.sleep(2)
    context.scan.choose_self_pickup()


@when(u'Add an item into cart and fill pickup information,')
def step_impl(context):
    context.chrome_driver.implicitly_wait(20)
    intermediate_process_mvp(context)
    context.pickup_detail = Pickup_Details(context.chrome_driver)
    context.pickup_detail.input_name_and_phone_number('test', '+8615995375141')


@when(u'Add an item into cart and fill delivery information')
def step_impl(context):
    context.chrome_driver.implicitly_wait(20)
    intermediate_process_mvp(context)
    context.deliver_details = Deliver_Details(context.chrome_driver)
    context.deliver_details.input_delivery_info('test', '+8615995375901')


@given(u'Navigate to scan homepage Safari Specially')
def step_impl(context):
    context.safari_driver.get('https://scan.beep.test16.shub.us/home')
    context.scan = Scan(context.safari_driver)
    context.scan.change_deliver_to_location_safari()


@step(u'Select delivery to location and store, choose Food delivery Safari Specially')
def step_impl(context):
    context.deliver = Deliver(context.safari_driver)
    context.deliver.select_address_safari()
    time.sleep(5)
    context.safari_driver.implicitly_wait(10)
    context.scan.select_store_safari('Auto For Beep Delivery')
    time.sleep(2)
    context.scan.choose_food_delivery_safari()


@step(u'Select delivery to location and store, choose Self pickup Safari Specially')
def step_impl(context):
    context.deliver = Deliver(context.safari_driver)
    context.deliver.select_address_safari()
    time.sleep(5)
    context.safari_driver.implicitly_wait(10)
    context.scan.select_store_safari('Auto For Beep Delivery')
    time.sleep(2)
    context.scan.choose_self_pickup_safari()


@when(u'Add an item into cart and fill pickup information Safari Specially')
def step_impl(context):
    context.safari_driver.implicitly_wait(20)
    intermediate_process_safari(context)
    context.pickup_detail = Pickup_Details(context.safari_driver)
    context.pickup_detail.input_name_and_phone_number_safari('test', +8615995375191)


@when(u'Add an item into cart and fill delivery information Safari Specially')
def step_impl(context):
    context.safari_driver.implicitly_wait(20)
    intermediate_process_safari(context)
    context.deliver_details = Deliver_Details(context.safari_driver)
    context.deliver_details.input_delivery_info_safari('test', '+8615995375105', '12')


@then(u'payment process Safari Specially')
def step_impl(context):
    context.select = PaymentSelection(context.safari_driver)
    context.select.pay_now_safari()
    context.safari_driver.implicitly_wait(10)
    context.card = Card(context.safari_driver)
    context.card.card_information_input_safari(4111111111111111, 1234, 123, 'test')
    context.safari_driver.implicitly_wait(10)
    context.safari_driver.implicitly_wait(10)
    context.payment = Payment(context.safari_driver)
    context.payment.input_opt_and_continue_safari(123456)
    context.safari_driver.implicitly_wait(10)
    context.paid = Paid(context.safari_driver)
    context.paid.transfer_to_order_paid()


