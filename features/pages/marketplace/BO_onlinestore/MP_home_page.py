from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.marketplace.mp_onlinestore.mp_online_locators import MPOnlineLocator
from selenium.webdriver.common.keys import Keys
from util.util import Util
import time

class MPHomepage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = self.driver.find_element(By.XPATH, MPOnlineLocator.search_bar)
        self.util = Util(self.driver)

    def search_product_online(self,product_name):
        value = self.search_bar.get_attribute("value")
        if value != "":
             pass
        else:
            self.search_bar.send_keys(product_name)
            time.sleep(1)
            self.search_bar.send_keys(Keys.RETURN)
        soup = self.util.beautiful_soup(self.driver.page_source)
        result_found = soup.find("main", class_="products__container sub-container").find("h3", class_="products__subtitle")
        print("\n\n"+str(result_found.text)+"\n\n")
        if result_found.text=='No result found':
            assert False, ("Product is not online")
        else:
            self.searched_product = self.driver.find_element(By.XPATH, MPOnlineLocator.searched_product)
            time.sleep(1)
            return self.searched_product

    def verify_product_is_online_successfully(self,product_name):
        self.product_search = self.search_product_online(product_name)
        title = self.product_search.get_attribute("title")
        #self.driver.save_screenshot("output/screenshot2.png")
        assert product_name in title, "Product is not online"
        
        
        
        
        
        




