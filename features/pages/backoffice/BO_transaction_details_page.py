from features.pages.backoffice.BO_locators import Locator
from util.commonfunctions import Actions


class TransactionDetails(object):
    def __init__(self, driver):
        self.driver = driver

    # Verify if receipt number in Transaction Details page is consistent with the searched condition inputed
    def compare_receipt_number_in_detail_page(self):
        receipt_number_value = Actions(self.driver).get_text(Locator.receipt_number_value)
        return receipt_number_value

    def compare_transaction_type_in_detail_page(self):
        transaction_type_value = Actions(self.driver).get_text(Locator.transaction_type_value)
        return transaction_type_value

    def compare_cancelled_by_in_detail_page(self):
        cancelled_by_value = Actions(self.driver).get_text(Locator.cancelled_by_value)
        return cancelled_by_value

    def compare_cancelled_at_in_detail_page(self):
        cancelled_at_value = Actions(self.driver).get_text(Locator.cancelled_at_value)
        return cancelled_at_value

    def compare_cancelled_reason_in_detail_page(self):
        cancelled_reason_value = Actions(self.driver).get_text(Locator.cancelled_reason_value)
        return cancelled_reason_value
