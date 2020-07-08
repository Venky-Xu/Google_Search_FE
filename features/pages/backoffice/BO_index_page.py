from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from features.pages.backoffice.BO_locators import Locator
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from util.util import *


class Index(object):
    def __init__(self, driver):
        self.driver = driver

    def negative_ipad_register(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, Locator.text_Settings).click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, Locator.partial_link_text_iPad_register).click()

