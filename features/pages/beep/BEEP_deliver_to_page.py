import selenium

from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from util.commonfunctions import Actions
import time


class Deliver(object):
    def __init__(self, driver):
        self.driver = driver

    def select_address(self):
        time.sleep(5)
        Actions(self.driver).explicit_wait(["element_clickable"], 30, Locator.search_address)
        Actions(self.driver).common_click(Locator.search_address)
        Actions(self.driver).send_keys(Locator.search_address, 'KLCC')
        Actions(self.driver).send_keys(Locator.search_address, Keys.ENTER)
        time.sleep(5)
        Actions(self.driver).get_single_object_from_list(Locator.searched_address_result, 1).click()

    def select_address_safari(self):
        WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, Locator.search_address)))
        Actions.safari_click(self, Locator.search_address)
        self.driver.find_element(By.XPATH, Locator.search_address).send_keys('Kuala Lumpur city center')
        self.driver.find_element(By.XPATH, Locator.search_address).send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            Actions.safari_click(self, Locator.search_address_result_safari)
        except selenium.common.exceptions.NoSuchElementException:
            Actions.safari_click(self, Locator.search_address_result_spare)