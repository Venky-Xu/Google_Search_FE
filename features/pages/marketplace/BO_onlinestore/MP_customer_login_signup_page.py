from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.marketplace.mp_onlinestore.mp_online_locators import MPOnlineLocator
from selenium.webdriver.common.keys import Keys
import time
from util.util import *
import logging


class CustomerLogin(object):

    def __init__(self, driver):
        self.driver = driver
        self.util = Util(self.driver)
        
    def login_while_checkout(self, username, password):
        try:
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, MPOnlineLocator.login_checkout))).click()
            self.login_with_customer_credentials(username, password)
        except Exception as ex:
            logging.exception(ex, False)

    def login_with_customer_credentials(self, username, password):
        self.login_email = self.driver.find_element(
            By.XPATH, MPOnlineLocator.login_email).send_keys(username)
        self.login_password = self.driver.find_element(
            By.XPATH, MPOnlineLocator.login_password)
        #self.login_password.click()
        #try:
            #self.driver.find_element(By.XPATH, MPOnlineLocator.email_error)
        #except:
            #pass
        #else:
            #print("\n\n"+"test"+"\n\n")
           # self.driver.quit()
        self.login_password.send_keys(password)
        self.signin=self.driver.find_element(
            By.XPATH, MPOnlineLocator.signin).click()

    def verify_customer_login_successful_while_checkout(self):
        soup=self.util.beautiful_soup(self.driver.page_source)
        uk_notify=soup.find(
            "div", class_="uk-notify uk-notify-top-center")
        if str(uk_notify) != "None":
            assert False, ("Customer Login failed due to invalid username or password")
        else:
            assert True, ("Customer Login successful")