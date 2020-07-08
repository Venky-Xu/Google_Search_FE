from selenium import webdriver
from pages.marketplace.bo_marketplace.bo_online_locators import BoOnlineLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from util.util import *
import time

class GettingStarted(object):

    def __init__(self, driver):
        self.driver = driver
        self.util = Util(self.driver)
        
    def go_to_online_store(self):
        time.sleep(1)
        #self.util.wait_for_load(Locator.blockui)
        element = self.driver.find_element_by_xpath(BoOnlineLocator.online_store)
        self.driver.execute_script("arguments[0]", element)
        #element.location_once_scrolled_into_view
        WebDriverWait(self.driver, 50).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.online_store))).click()

    def launch_marketplace(self):
        self.go_to_online_store()
        self.driver.find_element(By.XPATH, BoOnlineLocator.getting_started).click()
        self.driver.find_element(By.XPATH, BoOnlineLocator.view_online_store).click()