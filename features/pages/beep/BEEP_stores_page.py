from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.common.by import By
from util.commonfunctions import Actions
import time


class Stores(object):
    def __init__(self, driver):
        self.driver = driver

    def choose_store(self):
        Actions(self.driver).explicit_wait(["element_located"], 20, Locator.choose_notification)
        first_store = Actions(self.driver).get_single_object_from_list(Locator.stores, 2)
        first_store.click()

