from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from util.commonfunctions import Actions


class Preference(object):
    def __init__(self, driver):
        self.driver = driver

    def select_preference_pickup(self):
        Actions(self.driver).explicit_wait(["element_located"], 10, Locator.preference)
        preference_title = Actions(self.driver).get_text(Locator.header_title)
        assert preference_title == 'SELECT YOUR PREFERENCE'
        self_pickup = Actions(self.driver).get_single_object_from_list(Locator.preference, 2)
        self_pickup.click()

    def select_preference_delivery(self):
        Actions(self.driver).explicit_wait(["element_located"], 10, Locator.preference)
        preference_title = Actions(self.driver).get_text(Locator.header_title)
        assert preference_title == 'SELECT YOUR PREFERENCE'
        food_delivery = Actions(self.driver).get_single_object_from_list(Locator.preference, 1)
        food_delivery.click()

