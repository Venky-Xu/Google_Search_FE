from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from util.commonfunctions import Actions


class Details(object):
    def __init__(self, driver):
        self.driver = driver

    def input_delivery_info(self, name, phone_number):
        Actions(self.driver).explicit_wait(["element_located"], 10, Locator.customer_name)
        Actions(self.driver).input_clear(Locator.customer_name)
        time.sleep(2)
        Actions(self.driver).send_keys(Locator.customer_name, name)
        time.sleep(2)
        Actions(self.driver).input_clear(Locator.customer_phone_number)
        Actions(self.driver).send_keys(Locator.customer_phone_number, '+86')
        time.sleep(1)
        Actions(self.driver).send_keys(Locator.customer_phone_number, phone_number)
        Actions(self.driver).common_click(Locator.customer_continue)
        self.driver.implicitly_wait(10)

    def input_delivery_info_safari(self, name, phone_number, unit):
        #WebDriverWait(self.driver, 10).until(
         #   ec.presence_of_element_located((By.XPATH, Locator.delivery_mobile)))
        self.driver.find_element(By.XPATH, Locator.delivery_name).send_keys(name)
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locator.delivery_mobile).send_keys('+86')
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locator.delivery_mobile).send_keys(phone_number)
        Actions.safari_click(self, Locator.unit)
        self.driver.find_element(By.XPATH, Locator.delivery_dialog_textarea).send_keys(unit)
        time.sleep(1)
        Actions.safari_click(self, Locator.delivery_dialog_save)
        time.sleep(2)
        Actions.safari_click(self, Locator.Continue)
        self.driver.implicitly_wait(10)