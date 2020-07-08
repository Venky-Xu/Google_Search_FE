from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.marketplace.mp_onlinestore.mp_online_locators import MPOnlineLocator
from selenium.webdriver.common.keys import Keys
from util.util import Util
import time

class Payment(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.util = Util(self.driver)
        
    def click_on_proceed_to_pay_payment_page(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, MPOnlineLocator.proceed_to_pay).click()
        
    
        
    