from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from util.commonfunctions import Actions

import time


class Scan(object):
    def __init__(self, driver):
        self.driver = driver

    def change_deliver_to_location(self):
        Actions(self.driver).explicit_wait(["element_clickable"], 20, Locator.choose_deliver_to_location)
        Actions(self.driver).common_click(Locator.choose_deliver_to_location)

    def change_deliver_to_location_safari(self):
        WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, Locator.choose_deliver_to_location)))
        Actions.safari_click(self, Locator.choose_deliver_to_location)

    def select_store(self, store):
        Actions(self.driver).explicit_wait(["element_clickable"], 20, Locator.choose_deliver_to_location)
        Actions(self.driver).common_click(Locator.search_store)
        self.driver.implicitly_wait(10)
        Actions(self.driver).send_keys(Locator.input_store, store)
        Actions(self.driver).explicit_wait(["element_clickable"], 20, Locator.search_store_result)
        Actions(self.driver).get_single_object_from_list(Locator.search_store_result, 1).click()

    def select_self_pickup_store(self):
        Actions(self.driver).explicit_wait(["element_clickable"], 20, Locator.choose_deliver_to_location)
        Actions(self.driver).get_single_object_from_list(Locator.collection, 1).click()
        self.driver.implicitly_wait(10)
        Actions(self.driver).explicit_wait(["element_clickable"], 20, Locator.search_store_result)
        Actions(self.driver).get_single_object_from_list(Locator.search_store_result, 1).click()

    def select_store_safari(self, store):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, Locator.choose_deliver_to_location)))
        time.sleep(2)
        self.driver.execute_script("history.back")
        self.driver.execute_script("history.go(-1)")
        time.sleep(2)
        self.driver.execute_script("history.back")
        self.driver.execute_script("history.go(-1)")
        self.driver.implicitly_wait(10)
        Actions.safari_click(self, Locator.search_store)
        self.driver.find_element(By.XPATH, Locator.search_store).send_keys(store)
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, Locator.search_store_result_spare)))
        Actions.safari_click(self, Locator.search_store_result_spare)

    def choose_food_delivery(self):
        Actions(self.driver).explicit_wait(["element_located"], 10, Locator.scan_food_delivery)
        self.driver.find_element(By.XPATH, Locator.scan_food_delivery).click()

    def choose_food_delivery_safari(self):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, Locator.scan_food_delivery)))
        Actions.safari_click(self, Locator.scan_food_delivery)

    def choose_self_pickup(self):
        Actions(self.driver).explicit_wait(["element_located"], 10, Locator.scan_self_pickup)
        self.driver.find_element(By.XPATH, Locator.scan_self_pickup).click()

    def choose_self_pickup_safari(self):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, Locator.scan_self_pickup)))
        Actions.safari_click(self, Locator.scan_self_pickup)


