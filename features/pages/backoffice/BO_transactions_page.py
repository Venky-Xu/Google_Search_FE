from features.pages.backoffice.BO_locators import Locator
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from util.util import Util
import time
from util.commonfunctions import Actions


class Transactions(object):
    def __init__(self, driver):
        self.driver = driver

    def input_receipt_number(self, receipt_number):
        Actions(self.driver).explicit_wait(["element_located"], 10, Locator.transaction_filter_search)
        Actions(self.driver).common_click(Locator.transaction_filter_search)
        Actions(self.driver).send_keys(Locator.transaction_filter_search, receipt_number)

    # Count transactions in transactions table
    def count_transactions(self):
        return len(Actions(self.driver).get_element_lists(Locator.transaction_table))

    # Open one transaction detail via link in record's time
    def open_transaction_detail(self):
        Actions(self.driver).common_click(Locator.searched_transaction_time)


