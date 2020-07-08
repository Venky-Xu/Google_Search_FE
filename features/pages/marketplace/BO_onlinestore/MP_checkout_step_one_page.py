# Checkout Step-1 Page

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.marketplace.mp_onlinestore.mp_online_locators import MPOnlineLocator
from pages.marketplace.mp_onlinestore.mp_customer_login_signup_page import CustomerLogin
import time
from selenium.webdriver.support.ui import WebDriverWait
import logging
import os

class CheckoutStepOne(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.login = CustomerLogin(self.driver)
        
    def verify_checkout_step_one_direct_successfully(self):
        try:
            self.contact_email = self.driver.find_element(By.XPATH, MPOnlineLocator.contact_email)
            self.contact_name = self.driver.find_element(By.XPATH, MPOnlineLocator.contact_name)
            self.contact_phone = self.driver.find_element(By.XPATH, MPOnlineLocator.contact_phone)
        except:
            assert False, "Did not successfully direct to checkout step-1"
            
    def verify_contact_info_after_customer_login(self):
        time.sleep(1)
        self.contact_email = self.driver.find_element(By.XPATH, MPOnlineLocator.contact_email)
        self.contact_name = self.driver.find_element(By.XPATH, MPOnlineLocator.contact_name)
        self.contact_phone = self.driver.find_element(By.XPATH, MPOnlineLocator.contact_phone)
        email_after_login = self.contact_email.get_attribute("value")
        assert email_after_login in str(os.getenv("CUSTOMER_USERNAME")), "Contact Email after login does not match with Customer Login email"
        name_after_login = self.contact_name.get_attribute("value")
        phone_after_login = self.contact_phone.get_attribute("value")
        if name_after_login=="":
            assert False, "Customer name field is empty after Customer Login."
        elif phone_after_login=="":
            assert False, "Customer phone field is empty after Customer Login"
        else:
            pass
       
    def click_on_continue(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, MPOnlineLocator.continue_step_one))).click()
            time.sleep(1)
        except ValueError as identifier:
            logging.exception(identifier)
            
    def enter_contact_details(self):
        self.driver.find_element(By.XPATH, MPOnlineLocator.contact_email).send_keys("divya.singla@storehub.com")
        self.driver.find_element(By.XPATH, MPOnlineLocator.contact_name).send_keys("Divya Singla")
        self.driver.find_element(By.XPATH, MPOnlineLocator.contact_phone).send_keys("0186897990")
            
    
        
        
            
    
            
            
        
        
    
        