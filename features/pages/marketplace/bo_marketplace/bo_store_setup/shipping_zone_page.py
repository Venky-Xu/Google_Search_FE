from selenium import webdriver
from pages.marketplace.bo_marketplace.bo_online_locators import BoOnlineLocator
from pages.marketplace.bo_marketplace.bo_getting_started.gettingstarted_page import GettingStarted
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.backoffice.bo_locators import Locator
from util.util import *
import time

class ShippingZone(object):

    def __init__(self, driver):
        self.driver = driver
        self.util = Util(self.driver)
        self.getstarted = GettingStarted(self.driver)
        
    def get_shipping_zone_id(self, page_source):
        soup = self.util.beautiful_soup(page_source)
        shipping_zone_id = soup.find("form", class_= "horizontal-form store-info-form")
        id = str(shipping_zone_id['action'])
        if id=="/onlineStore/shippingZones/new":
            assert False, ("Shipping Zone is not saved successfully")
        else:
            id = id.split("=")
            print("\n\n"+id[1]+"\n\n")
            return id[1]
    
    def get_existing_shipping_zone_id(self, page_source):
        soup = self.util.beautiful_soup(page_source)
        existing_zones = soup.find_all("div", class_= "shipping-zones")                  
        return existing_zones
    
    def go_to_shipping_zone(self):
        self.getstarted.go_to_online_store()
        time.sleep(1)
        self.driver.find_element(By.XPATH, BoOnlineLocator.store_setup).click()
        
    def click_create_new_shipping_zone(self):
        self.driver.find_element(By.XPATH, BoOnlineLocator.add_shipping_zone).click()
        
    def enter_shipping_zone_name(self, zone_name):
        self.zone_name = self.driver.find_element(By.XPATH, BoOnlineLocator.zone_name)
        existing_zone_name = self.zone_name.get_attribute("value")
        if existing_zone_name=="":
            self.zone_name.send_keys(zone_name)
        else:
            self.zone_name.clear()
            self.zone_name.send_keys(zone_name)
        
    def enter_shipping_estimate(self):
        self.driver.find_element(By.XPATH, BoOnlineLocator.min_shipping_estimate).send_keys("1")
        self.driver.find_element(By.XPATH, BoOnlineLocator.max_shipping_estimate).send_keys("4")

    def select_state_province(self):
        self.util.wait_for_load(Locator.blockui)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.state_button))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.select_selangor))).click()
        time.sleep(1)
        #self.driver.find_element(By.XPATH, BoOnlineLocator.state_button).click()
        #select = Select(self.driver.find_element(By.XPATH, BoOnlineLocator.state_selection))
        #select.select_by_t("Kuala Lumpur")
        
    def select_postcodes(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.postcode_button))).click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.select_all_postcodes))).click()
        time.sleep(1)
        
    def select_country(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.select_country))).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.andorra))).click()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.antarctica))).click()
        
    def enter_rate_amount(self):
        self.driver.find_element(By.XPATH, BoOnlineLocator.rate_amount).send_keys("20")    
        
    def enable_free_shipping(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, BoOnlineLocator.enable_free_shipping).click()
        self.shipping_rate = self.driver.find_element(By.XPATH, BoOnlineLocator.free_shipping_rate)
        self.shipping_rate.clear()
        self.shipping_rate.send_keys("100")
        
    def save_shipping_zone(self):
        #time.sleep(1)
        self.util.wait_for_load(Locator.blockui)
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.save_button))).click()
        time.sleep(1)
      
    def enter_local_shipping_zone_details(self):
        self.click_create_new_shipping_zone()
        self.enter_shipping_zone_name("Local_zone")
        self.enter_shipping_estimate()
        self.select_state_province()
        self.select_postcodes()
        self.enter_rate_amount()
        self.enable_free_shipping()
        self.save_shipping_zone()
        return self.get_shipping_zone_id(self.driver.page_source)
        
    def enter_international_shipping_zone_details(self):
        self.click_create_new_shipping_zone()
        self.enter_shipping_zone_name("International_zone")
        self.util.wait_for_load(Locator.blockui)
        self.driver.find_element(By.XPATH, BoOnlineLocator.shipping_type).click()
        self.driver.find_element(By.XPATH, BoOnlineLocator.international_shipping).click()
        self.enter_shipping_estimate()
        self.select_country()
        self.enter_rate_amount()
        self.enable_free_shipping()
        self.save_shipping_zone()
        return self.get_shipping_zone_id(self.driver.page_source)
        
        
    def verify_new_shipping_zone_added_successfully(self, id):
        assert id in self.driver.current_url, "Shipping Zone is not saved successfully"
        
    def check_for_existing_shipping_zone(self):
        self.go_to_shipping_zone()
        configure_shipping_zone_text = self.driver.find_element(By.XPATH, BoOnlineLocator.configure_shipping_zone).text
        if configure_shipping_zone_text=="Configure your shipping rules":
            assert False, ("There is no existing shipping zone. Please create a new shipping zone")
        else:
            existing_shipping_zones_data = self.get_existing_shipping_zone_id(self.driver.page_source)
            return existing_shipping_zones_data[0]["id"]
          
    def click_on_edit_shipping_zone(self, id):
        self.driver.find_element(By.XPATH, "//*[contains(@id,'"+id+"')]/a").click()
        
    def edit_existing_shipping_zone(self):
        self.enter_shipping_zone_name("Edit_zone_name")
        self.save_shipping_zone()
        
    def verify_edited_shipping_zone(self):
        zone_name = self.driver.find_element(By.XPATH, BoOnlineLocator.zone_name).get_attribute("value")
        assert zone_name in "Edit_zone_name", "Shipping zone is not edited successfully"
        
    def delete_shipping_zone(self):
        self.util.wait_for_load(Locator.blockui)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.delete_shipping_zone))).click()
        self.util.wait_for_load(Locator.blockui)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, BoOnlineLocator.confirm_delete))).click()
        
    def verify_deleted_shipping_zone(self, id):
        time.sleep(1)
        existing_shipping_zones_data = self.get_existing_shipping_zone_id(self.driver.page_source)
        no_of_existing_shipping_zones = len(existing_shipping_zones_data) 
        if no_of_existing_shipping_zones==0:
            assert True, ("Shipping Zone is deleted successfully")
        else:
            i=0
            while no_of_existing_shipping_zones>=0:
                if id==existing_shipping_zones_data[i]["id"]:
                    i=i+1
                    assert False, ("Shipping Zone is not deleted")
                no_of_existing_shipping_zones= no_of_existing_shipping_zones-1
        assert True, ("Shipping Zone is deleted successfully")
        
        
        
        
    