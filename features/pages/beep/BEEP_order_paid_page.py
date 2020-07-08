from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from util.util import Util
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from util.commonfunctions import Actions
import time


class Paid(object):
    def __init__(self, driver):
        self.driver = driver

    def transfer_to_order_paid(self):
        Actions(self.driver).explicit_wait(["element_located"], 20, Locator.header_title)
        order_id = Actions(self.driver).get_text(Locator.header_title)
        return order_id
        #prepare = self.driver.find_element(By.XPATH, Locator.prepare).text
        #print(prepare)
        #assert  "We're preparing your order now." in prepare

    def input_phone_number(self):
        self.driver.find_element(By.XPATH, Locator.phone_number).clear()
        self.driver.find_element(By.XPATH, Locator.phone_number).send_keys(Util.BEEP_PHONE_NUMBER)
        self.driver.find_element(By.XPATH, Locator.beep_continue).click()
        self.driver.implicitly_wait(15)

    def view_receipt(self, number):
        self.driver.find_element(By.XPATH, Locator.view_receipt).click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.XPATH, Locator.close).click()
        self.driver.implicitly_wait(15)
        order_number = self.driver.find_element(By.XPATH, Locator.pick_up_number).text
        assert order_number == number

    def cash_back(self):
        self.driver.find_element(By.XPATH, Locator.check_my_balance).click()




