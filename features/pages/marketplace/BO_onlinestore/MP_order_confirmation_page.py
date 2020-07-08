from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.marketplace.mp_onlinestore.mp_online_locators import MPOnlineLocator
from selenium.webdriver.common.keys import Keys
from util.util import Util
import time

class OrderConfirmation(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.util = Util(self.driver)
        
    def verify_if_order_placed_successfully(self):
        #time.sleep(2)
        title = self.driver.find_element(By.XPATH, MPOnlineLocator.order_confirmation_title).text
        if title=="Awesome!":
            assert True, "Order placed successfully"
        else:
            assert False, title
            
    def verify_delivery_fee_in_order_summary(self, delivery_fee):
        self.driver.find_element(By.XPATH, MPOnlineLocator.view_summary).click()
        order_summary_delivery_fee = self.driver.find_element(By.XPATH, MPOnlineLocator.order_summary_delivery_fee).text
        print("\n\n"+order_summary_delivery_fee+"\n\n")
        assert delivery_fee in order_summary_delivery_fee, "Delivery fee is incorrect in order summary"
        
    
        
    