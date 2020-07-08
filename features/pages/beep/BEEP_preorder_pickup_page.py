from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import selenium
import time
from util.commonfunctions import Actions


class PrePickup(object):
    def __init__(self, driver):
        self.driver = driver

    def choose_pickup_date(self):
        Actions(self.driver).explicit_wait(["element_located"], 60, Locator.preorder_date)
        Actions(self.driver).get_single_object_from_list(Locator.preorder_date, 2).click()
        time.sleep(1)
        Actions(self.driver).get_single_object_from_list(Locator.preorder_hour, 2).click()
        time.sleep(1)
        Actions(self.driver).common_click(Locator.Continue)

    def click_deliver_to(self):
        Actions(self.driver).explicit_wait(["element_located"],10, Locator.deliver_to)
        delivery_details_title = Actions(self.driver).get_text(Locator.header_title)
        assert delivery_details_title == 'Delivery Details'
        Actions(self.driver).common_click(Locator.deliver_to)

    def choose_delivery_date(self):
        Actions(self.driver).explicit_wait(["element_located"], 60, Locator.preorder_date)
        Actions(self.driver).get_single_object_from_list(Locator.preorder_date, 2).click()
        time.sleep(1)
        Actions(self.driver).get_single_object_from_list(Locator.preorder_hour, 2).click()
        time.sleep(1)

    def continue_click(self):
        Actions(self.driver).explicit_wait(["element_clickable"], 10, Locator.Continue)
        Actions(self.driver).common_click(Locator.Continue)