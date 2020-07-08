from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from util.commonfunctions import Actions


class Online(object):
    def __init__(self, driver):
        self.driver = driver

    def choose_bank_and_pay(self):
        Actions(self.driver).explicit_wait(["element_located"], 20, Locator.bank)
        Actions(self.driver).common_click(Locator.pay_money)
        time.sleep(5)