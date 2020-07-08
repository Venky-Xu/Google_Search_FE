from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from util.commonfunctions import Actions


class Stripe(object):
    def __init__(self, driver):
        self.driver = driver

    def authorize_test_payment(self):
        Actions(self.driver).get_single_object_from_list(Locator.test_payment, 1).click()