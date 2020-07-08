from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class PayViaOnlineBanking(object):
    def __init__(self, driver):
        self.driver = driver

    def pay_coin(self):
        self.driver.find_element(By.XPATH, Locator.pay_).click()
