from features.pages.backoffice.BO_transactions_page import Transactions
from behave import *
import time
import json
from util.commonfunctions import Actions
from util.util import Interface
from hamcrest import assert_that, equal_to, contains_string, is_not
from features.pages.backoffice.BO_transaction_details_page import TransactionDetails


@step(u'Navigate to All Transactions page')
def step_impl(context):
    context.chrome_driver.implicitly_wait(10)
    Actions(context.chrome_driver).navigate_to_bo_menu_item("Transactions")
    Actions(context.chrome_driver).navigate_to_bo_menu_item("All Transactions")


@when(u'Input valid receipt number')
def step_impl(context):
    context.transactions = Transactions(context.chrome_driver)
    context.receipt_number = '0002007031742055'
    context.transactions.input_receipt_number(context.receipt_number)


@then(u'The corresponding transaction should appear in search result')
def step_impl(context):
    context.chrome_driver.implicitly_wait(10)
    time.sleep(3)
    count = context.transactions.count_transactions()
    context.chrome_driver.implicitly_wait(10)
    assert_that(count, equal_to(1))
    context.transactions.open_transaction_detail()
    context.chrome_driver.implicitly_wait(10)
    context.transactions_details = TransactionDetails(context.chrome_driver)
    assert_that(context.receipt_number, equal_to(context.transactions_details.compare_receipt_number_in_detail_page()))


@when(u'click on a transaction with type: Sale')
def step_impl(context):
    response = Interface().add_transaction_sale()
    responses = json.loads(response)
    context.receipt_number = responses["receiptNumber"]
    context.transactions = Transactions(context.chrome_driver)
    context.transactions.input_receipt_number(context.receipt_number)
    context.chrome_driver.implicitly_wait(10)
    context.transactions_details = TransactionDetails(context.chrome_driver)
    context.transactions.open_transaction_detail()


@then(u'the transaction detail page of the particular transaction should open with the correct details,Transaction '
      u'Type: Sale')
def step_impl(context):
    context.chrome_driver.implicitly_wait(10)
    assert_that("Sale",
                equal_to(context.transactions_details.compare_transaction_type_in_detail_page()))


@when(u'click on a transaction with type: Cancelled')
def step_impl(context):
    response = Interface().add_transaction_cancel()
    responses = json.loads(response)
    context.receipt_number = responses["receiptNumber"]
    context.return_reason = responses["returnReason"]
    context.transactions = Transactions(context.chrome_driver)
    context.transactions.input_receipt_number(context.receipt_number)
    context.chrome_driver.implicitly_wait(10)
    context.transactions_details = TransactionDetails(context.chrome_driver)
    context.transactions.open_transaction_detail()


@then(u'Transaction Type in transaction details page should be "Cancelled", Cancel information should not be empty')
def step_impl(context):
    context.chrome_driver.implicitly_wait(10)
    assert_that(contains_string("Cancelled"), context.transactions_details.compare_transaction_type_in_detail_page())
    assert_that(context.return_reason,
                equal_to(context.transactions_details.compare_cancelled_reason_in_detail_page()))
    assert_that(None, is_not(context.transactions_details.compare_cancelled_at_in_detail_page()))
    assert_that(None, is_not(context.transactions_details.compare_cancelled_by_in_detail_page()))
