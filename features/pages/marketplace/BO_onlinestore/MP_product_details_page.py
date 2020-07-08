# Product details page.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.marketplace.mp_onlinestore.mp_online_locators import MPOnlineLocator
import time
from pages.marketplace.mp_onlinestore.mp_home_page import MPHomepage
from selenium.webdriver.support.ui import WebDriverWait
import logging

class ProductDetails(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.homepage = MPHomepage(self.driver)
        
    def click_on_product_and_verify_details(self,product_name):
        self.searched_product = self.homepage.search_product_online(product_name)
        self.searched_product.click()
        #assert product_name in MPOnlineLocator.product_name_on_product_details_page # need to give locator
    
    def verify_stock_status(self):
        time.sleep(1)
        stock_status = self.driver.find_element(By.XPATH, MPOnlineLocator.stock_status)
        stock_status = stock_status.text
        if stock_status=="In Stock":
            pass
        else:
            assert False, ("Product is out of Stock")
            logging.error("logger ==> Product is out of Stock")
            
    def add_product_to_cart(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, MPOnlineLocator.add_to_cart))).click()
        
    def verify_product_details(self,product_name,product_price,variants_info):
        print("details are verified")
        
    def click_on_checkout(self):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, MPOnlineLocator.checkout))).click()
        