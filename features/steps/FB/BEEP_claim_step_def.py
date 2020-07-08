from behave import *
from features.pages.beep.BEEP_order_paid_page import Paid


@given(u'Transfer to order paid')
def step_impl(context):
    context.paid = Paid(context.chrome_driver)
    context.paid.transfer_to_order_paid()


@when(u'check view receipt')
def step_impl(context):
    context.paid.input_phone_number()
    context.paid.view_receipt('0001')


@then(u'check balance')
def step_impl(context):
    context.paid.cash_back()