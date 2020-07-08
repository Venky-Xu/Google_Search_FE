from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from features.pages.backoffice.BO_locators import Locator
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from util.util import Util
import time
from hamcrest import *
from util.commonfunctions import Actions

class Products(object):
    count=0
    
    def __init__(self, driver):
        self.driver = driver
        self.util= Util()
        self.data = self.util.test_data()
    
    def get_stores_data(self, page_source):
        soup = self.util.beautiful_soup(page_source)
        table = soup.find("table", class_="table table-bordered table-striped").find("tbody").find_all("tr")
        return table
    
    def get_group_id(self, page_source):
        soup = self.util.beautiful_soup(page_source)
        group_id = soup.find_all("li", class_="ui-state-default form-inline")
        id = group_id[self.count]['id']
        self.count= self.count+1
        return id
    
    def enter_general_details(self):
        Actions(self.driver).navigate_to_bo_menu_item("Products")
        Actions(self.driver).navigate_to_bo_menu_item("Add Product")
        Actions(self.driver).send_keys(Locator.product_name, self.data["product_name"])
        Actions(self.driver).send_keys(Locator.sku, self.data["sku"])
        Actions(self.driver).send_keys_from_keyboard(Locator.enter_tag, self.data["tags"], "ENTER")
        Actions(self.driver).explicit_wait(["element_visibility"], 10, Locator.supplier_button).click()
        Actions(self.driver).explicit_wait(["element_visibility"], 10, Locator.supplier_dropdown).click()
    
    def choose_pricing_type(self, pricing_type):
        Actions(self.driver).explicit_wait(["element_clickable"], 10, Locator.pricing_type).click()
        if pricing_type == 'Fixed':
            Actions(self.driver).common_click(Locator.Fixed)
        elif pricing_type == 'Variable':
            Actions(self.driver).common_click(Locator.Variable)
        elif pricing_type == 'By Unit':
            Actions(self.driver).common_click(Locator.Unit)
            
    def choose_tracking_type(self, tracking_type):
        Actions(self.driver).common_click(Locator.track_inventory_checkbox)
        Actions(self.driver).common_click(Locator.inventory_type_btn)
        time.sleep(1)
        if tracking_type == 'Simple':
            Actions(self.driver).common_click(Locator.Simple)
        elif tracking_type == 'Composite':
            Actions(self.driver).common_click(Locator.Composite)
        elif tracking_type == 'Serialized':
            Actions(self.driver).common_click(Locator.Serialized)
            
    def enter_cost(self):
        Actions(self.driver).send_keys(Locator.cost, self.data["cost"])
      
    def enter_product_price(self):
        Actions(self.driver).send_keys(Locator.tax_inclusive_price, self.data["tax_exclusive_price"])
        
    def is_has_variants_checked(self):
        self.has_variants = self.driver.find_element(By.XPATH, Locator.has_variants)
        if self.has_variants.get_attribute("class") == "checked":
            pass
        else:
            self.has_variants.click()
    
    def add_single_choice_variants(self, no_of_variants, no_of_options):
        self.is_has_variants_checked()
        i=1
        while i<=no_of_variants:
            Actions(self.driver).common_click(Locator.add_single_choice)
            group_id = self.get_group_id(self.driver.page_source)
            Actions(self.driver).send_keys("//*[contains(@id, '"+group_id+"')]/div[1]/input", "group_name"+str(i))
            Actions(self.driver).send_keys("//*[contains(@id, '"+group_id+"')]/div[2]/div[2]/ul/li/div[1]/input", "variant"+str(i))
            j=2
            while j<=no_of_options:
                Actions(self.driver).common_click("//*[contains(@id, '"+group_id+"')]/div[2]/div[2]/div/a")
                Actions(self.driver).send_keys("//*[contains(@id, '"+group_id+"')]/div[2]/div[2]/ul/li["+str(j)+"]/div[1]/input", "variant"+str(j))
                j=j+1
            i=i+1
    
    def add_multiple_choice_variants(self, no_of_multiple_variants, no_of_options):
        self.is_has_variants_checked()
        i=1
        while i<=no_of_multiple_variants:
            Actions(self.driver).common_click(Locator.add_multiple_choice)
            group_id = self.get_group_id(self.driver.page_source)
            Actions(self.driver).send_keys("//*[contains(@id, '"+group_id+"')]/div[1]/input", "multiple_variant"+str(i))
            Actions(self.driver).send_keys("//*[contains(@id, '"+group_id+"')]/div[4]/div[2]/ul/li/div[1]/input", "option"+str(i))
            j=2
            while j<=no_of_options:
                Actions(self.driver).common_click("//*[contains(@id, '"+group_id+"')]/div[4]/div[2]/div/a")
                Actions(self.driver).send_keys("//*[contains(@id, '"+group_id+"')]/div[4]/div[2]/ul/li["+str(j)+"]/div[1]/input", "option"+str(j))
                j=j+1
            i=i+1
            
    def save_and_get_product_id(self):
        Actions(self.driver).common_click(Locator.save_button)
        time.sleep(1)
        product_id = self.get_stores_data(self.driver.page_source)
        return product_id[0]['data-productid']
    
     #--------------VERIFY PRODUCT ADDED SUCCESSFULLY

    def verify_product_added_successfully(self,product_id):
        assert_that(product_id, not_none, "Product is not saved successfully")
        assert_that(product_id, self.driver.current_url, "Product is not saved successfully" )
        
    def simple_track_inventory_without_variants(self):
        self.choose_tracking_type("Simple")
        stores_data = self.get_stores_data(self.driver.page_source)
        length= len(stores_data)
        i=1
        while i<=length:
            Actions(self.driver).input_clear("//*[@id='multiStoreQuantityList']/tbody/tr["+str(i)+"]/td[2]/div/input").send_keys("10")
            Actions(self.driver).input_clear("//*[@id='multiStoreQuantityList']/tbody/tr["+str(i)+"]/td[3]/div/input").send_keys("10")
            Actions(self.driver).input_clear("//*[@id='multiStoreQuantityList']/tbody/tr["+str(i)+"]/td[4]/div/input").send_keys("10")
            i=i+1
            
    # def simple_track_inventory_with_variants(self):
    #     self.choose_tracking_type("Simple")
    #     time.sleep(1)
    #     return self.save_and_get_product_id()
    #     time.sleep(2)
    #     soup = self.util.beautiful_soup(self.driver.page_source)
    #     no_of_child_products = soup.find("table", class_="table table-bordered dataTable").find("tbody").find_all("tr", class_="child-item")
    #     print("\n\n"+str(len(no_of_child_products))+"\n\n")
        
    #---------------ADD PRODUCT
    
    # Add products with Single and Multiple Choice Variants without tracking inventory
    
    def add_product_with_variants_no_inventory(self):
        self.enter_general_details()  # enter general details of a product like product name, category, SKU etc
        self.enter_cost()
        self.enter_product_price()  # enter pricing details like cost, pricing type and selling price etc
        self.add_single_choice_variants(2,1) # Add single choice varinats. Need to give No of Variants and No of Options as Arguments.
        self.add_multiple_choice_variants(1,3)  # Add multiple choice varinats. Need to give No of Variants and No of Options as Arguments.
        product_id = self.save_and_get_product_id()
        return product_id

    # Add Simple Tracking Product with No Variants
    
    def add_product_with_simple_inventory_no_variants(self):
        self.enter_general_details()  
        self.enter_cost()
        self.enter_product_price() 
        self.simple_track_inventory_without_variants()
        product_id = self.save_and_get_product_id()
        return product_id
    
    # Add Simple tracking Product with Single and Multiple Choice Varinants
    
    def add_product_with_simple_inventory_and_variants(self):
        self.enter_general_details()  
        self.enter_cost()
        self.enter_product_price() 
        self.add_single_choice_variants(2,1)
        self.choose_tracking_type("Simple")
        product_id = self.save_and_get_product_id()
        return product_id
    
    def add_variable_price_product(self):
        self.enter_general_details()
        self.choose_pricing_type("Variable")
        self.enter_cost()
        product_id = self.save_and_get_product_id()
        return product_id
    
    #---------------DELETE PRODUCT
    
    def delete_product(self):
        print("delete product")
        
    # --------------PRODUCT ONLINE INFO
        
    def get_product_online_name(self):
        online_product_name = Actions(self.driver).get_attribute(Locator.online_name, "value")
        offline_product_name = Actions(self.driver).get_attribute(Locator.online_name, "placeholder")
        if online_product_name != "":
            return online_product_name
        else:
            return offline_product_name


    def make_product_sell_online(self):
        Actions(self.driver).explicit_wait("element_clickable", 10, Locator.online_info_tab).click()
        #Actions(self.driver).explicit_wait("element_invisibility", 10, Locator.blockui)
        Actions(self.driver).explicit_wait("element_located", 10, Locator.sell_online).click()
        Actions(self.driver).explicit_wait("element_located", 10, Locator.featured_products).click()
        Actions(self.driver).common_click(Locator.save_online)
        online_name = self.get_product_online_name()
        return online_name
    
    # Search product in Manage Products
          
    def search_product(self, product_name, product_id):
        #Actions(self.driver).explicit_wait("element_invisibility", 10, Locator.blockui)
        Actions(self.driver).explicit_wait(["element_invisibility"], 5, Locator.blockui)
        Actions(self.driver).navigate_to_bo_menu_item("Manage Products")
        Actions(self.driver).send_keys(Locator.product_search, product_name)
        Actions(self.driver).common_click("//*[contains(@id, '"+product_id+"')]/td[2]/a")


        


        
        

        