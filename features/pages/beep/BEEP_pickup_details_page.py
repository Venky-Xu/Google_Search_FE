from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from util.commonfunctions import Actions
import time


class Details(object):
    def __init__(self, driver):
        self.driver = driver

    # input
    def input_name_and_phone_number(self, name, phone_number):
        Actions(self.driver).explicit_wait(["element_located"], 10, Locator.customer_name)
        Actions(self.driver).send_keys(Locator.customer_name, name)
        time.sleep(1)
        Actions(self.driver).input_clear(Locator.customer_name)
        Actions(self.driver).send_keys(Locator.customer_phone_number, '+86')
        time.sleep(1)
        Actions(self.driver).send_keys(Locator.customer_phone_number, phone_number)
        Actions(self.driver).common_click(Locator.customer_continue)
        self.driver.implicitly_wait(10)

    def input_name_and_phone_number_safari(self, name, phone_number):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, Locator.pickip_details_title)))
        self.driver.find_element(By.XPATH, Locator.customer_name).send_keys(name)
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locator.customer_phone_number).clear()
        self.driver.find_element(By.XPATH, Locator.customer_phone_number).send_keys('+86')
        time.sleep(1)
        self.driver.find_element(By.XPATH, Locator.customer_phone_number).send_keys(phone_number)
        Actions.safari_click(self, Locator.beep_continue)
        self.driver.implicitly_wait(10)