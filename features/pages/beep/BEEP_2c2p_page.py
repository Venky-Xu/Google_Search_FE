from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from util.commonfunctions import Actions
import time


class Payment(object):
    def __init__(self, driver):
        self.driver = driver

    def input_opt_and_continue(self, otp):
        Actions(self.driver).presence_of_element_located(100, Locator.otp)
        Actions(self.driver).send_keys(Locator.otp, otp)
        time.sleep(3)
        Actions(self.driver).common_click(Locator.proceed)

    def input_opt_and_continue_safari(self, otp):
        WebDriverWait(self.driver, 200).until(
            ec.presence_of_element_located((By.XPATH, Locator.otp)))
        self.driver.find_element(By.XPATH, Locator.otp).send_keys(otp)
        time.sleep(3)
        Actions.safari_click(self, Locator.proceed)

