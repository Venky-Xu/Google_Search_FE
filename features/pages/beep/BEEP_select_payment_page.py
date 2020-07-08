from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from util.commonfunctions import Actions


class PaymentSelection(object):
    def __init__(self, driver):
        self.driver = driver

    def pay_now(self):
        Actions(self.driver).explicit_wait(["element_clickable"], 10, Locator.pay_now)
        time.sleep(2)
        Actions(self.driver).get_single_object_from_list(Locator.payment_selector, 2).click()
        time.sleep(2)
        Actions(self.driver).common_click(Locator.pay_now)
        self.driver.implicitly_wait(10)

    def pay_now_safari(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, Locator.visa_MasterCard)))
        time.sleep(2)
        Actions.safari_click(self, Locator.visa_MasterCard)
        time.sleep(2)
        Actions.safari_click(self, Locator.pay_now)
        self.driver.implicitly_wait(10)