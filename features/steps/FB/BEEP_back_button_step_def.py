from behave import *
from features.pages.beep.BEEP_order_page import Order
from util.commonfunctions import Actions
from hamcrest import assert_that, contains_string


@when(u'Verify the Visibility of bar is true and position of back button is in DELIVER TO bar, click the back button')
def step_impl(context):
    context.order = Order(context.chrome_driver)
    assert context.order.verify_visibility_of_bar() == True
    assert context.order.verify_back_is_in_deliver_or_pickup_bar() == True
    context.order.click_back_button()
    context.chrome_driver.implicitly_wait(10)


@then(u'Take back to homepage')
def step_impl(context):
    assert_that(Actions(context.chrome_driver).get_current_url(), contains_string('home'))


@when(u'Verify the Visibility of bar is false and position of back button is in STORE NAME bar, click the back button')
def step_impl(context):
    context.order = Order(context.chrome_driver)
    assert context.order.verify_visibility_of_bar() == False
    assert context.order.verify_back_is_in_store_name_bar() == True
    context.order.click_back_button_in_store_name()
    context.chrome_driver.implicitly_wait(10)


@then(u'Verify the Visibility of bar is true and no back button on current page')
def step_impl(context):
    context.order = Order(context.chrome_driver)
    assert context.order.verify_visibility_of_bar() == True
    print(context.order.verify_visibility_of_back())
    assert context.order.verify_visibility_of_back() == False



