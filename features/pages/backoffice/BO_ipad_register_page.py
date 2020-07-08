from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from features.pages.backoffice.BO_locators import Locator
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from util.util import *


class Register(object):
    def __init__(self, driver):
        self.driver = driver

    def verify_page(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, Locator.text_add_ipad_register)))

    def add_ipad_register(self):
        WebDriverWait(
            self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, Locator.text_add_ipad_register))).click()
        self.driver.find_element(By.XPATH, Locator.id_confirm_adding_new_register_yes)
        WebDriverWait(
            self.driver, 10).until(ec.presence_of_element_located((By.XPATH, Locator.id_edit_register_form)))

    def save_register(self):
        WebDriverWait(
            self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, Locator.id_save_register))).click()
