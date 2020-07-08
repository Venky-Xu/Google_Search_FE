# Checkout Step-2 Page

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.marketplace.mp_onlinestore.mp_online_locators import MPOnlineLocator
from pages.marketplace.mp_onlinestore.mp_customer_login_signup_page import CustomerLogin
import time
from selenium.webdriver.support.ui import WebDriverWait
from util.util import *
from selenium.webdriver.common.keys import Keys


class CheckoutStepTwo(object):

    def __init__(self, driver):
        self.driver = driver
        self.util = Util(self.driver)

    def verify_checkout_step_two_direct_successfully(self):
        try:
            self.get_selected_fulfillment_method()
        except:
            assert False, "Did not direct successfully to checkout Step-2"

    def get_selected_fulfillment_method(self):
        soup = self.util.beautiful_soup(self.driver.page_source)
        fulfillment_method = soup.find("div", class_="checkout-form__tabs uk-grid uk-flex uk-flex-middle uk-flex-space-between").find_all(
            "div", class_="uk-width-1-2")
        return len(fulfillment_method)
    
    def choose_fulfillment_method(self, fulfillment_method):
        no_of_fulfillment_method = self.get_selected_fulfillment_method()
        if no_of_fulfillment_method == 2:
            if fulfillment_method == "Delivery":
                pass
            else:
                self.driver.find_element(
                    By.XPATH, MPOnlineLocator.pickup_option).click()
        else:
            soup = self.util.beautiful_soup(self.driver.page_source)
            available_fulfillment_method = soup.find(
                "div", class_="checkout-form__tab uk-active").find("h3")
            available_fulfillment_method = available_fulfillment_method.text
            if fulfillment_method == available_fulfillment_method:
                pass
            else:
                assert False, (
                    "Required fulfillment method doesn't exist. Please select required fulfillment method in BO")
        time.sleep(1)

#------------ For Delivery Order


    def enter_valid_postcode(self):
        self.driver.find_element(
            By.XPATH, MPOnlineLocator.postcode_selector).click()
        self.postcode = self.driver.find_element(
            By.XPATH, MPOnlineLocator.postcode)
        self.postcode.send_keys("12345")
        self.driver.find_element(
            By.XPATH, MPOnlineLocator.delivery_coverage).click()
        time.sleep(1)
        soup = self.util.beautiful_soup(self.driver.page_source)
        valid_postcode = soup.find(
            "table", class_="uk-table uk-table-hover uk-table-striped uk-table-condensed").find("tbody").find("tr").find_all("td")
        postcode = str(valid_postcode[2].text).split(',')[0]
        self.driver.find_element(By.XPATH, MPOnlineLocator.close_button).click()
        self.postcode.clear()
        self.postcode.send_keys(postcode)
        time.sleep(1)
        self.postcode.send_keys(Keys.RETURN)
        # time.sleep(1)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(
            (By.XPATH, MPOnlineLocator.add_address_button))).click()


    def enter_shipping_address(self):
        self.driver.find_element(
            By.XPATH, MPOnlineLocator.add_new_address_button).click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(
            (By.XPATH, MPOnlineLocator.name))).send_keys("Test_name")
        self.driver.find_element(
            By.XPATH, MPOnlineLocator.phone).send_keys("0186876990")
        self.driver.find_element(By.XPATH, MPOnlineLocator.address).send_keys(
            "Unit C-3, 10 Boulevard")
        self.enter_valid_postcode()
        
    def choose_shipping_zone(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, MPOnlineLocator.shipping_zone).click()
        #soup = self.util.beautiful_soup(self.driver.page_source)
        #delivery_option = soup.find_all("div", class_="checkout-form__group").find("div").find("div")
        #print("\n\n"+str(delivery_option["class"])+"\n\n")
        
    def verify_delivery_fee_in_cart(self):
        shipping_fee = self.driver.find_element(By.XPATH, MPOnlineLocator.shipping_fee).text
        cart_shipping_fee = self.driver.find_element(By.XPATH, MPOnlineLocator.cart_shipping_fee).text
        cart_shipping_fee = cart_shipping_fee.split(" ")
        assert str(cart_shipping_fee[2]) in shipping_fee, "Delivery fee in Cart is incorrect"
        return str(cart_shipping_fee[2])
        
#-------For Pickup Order

    def check_availability_of_pickup_store(self):
        soup = self.util.beautiful_soup(self.driver.page_source)
        pickup_store_list = soup.find("div", class_="checkout-form__address-list").find_all("div", role="button")
        no_of_pickup_stores = len(pickup_store_list)
        i=0
        while i<no_of_pickup_stores:
            if "available" or "selected" in str(pickup_store_list[i]["class"]):
                self.driver.find_element(By.XPATH, "//*[@id='checkout-container']/div/div/div[1]/div/div[1]/form/fieldset[1]/div/div["+str(i+1)+"]").click()
                break
            i=i+1
        else:
            assert False, "Some Items are unavailable in Pickup Store"

    
    def click_on_proceed_to_pay_delivery(self):
        self.driver.find_element(By.XPATH, MPOnlineLocator.proceed_to_pay_delivery).click()
        
    def click_on_proceed_to_pay_pickup(self):
        self.driver.find_element(By.XPATH, MPOnlineLocator.proceed_to_pay_pickup).click()
        
    def check_for_error_message_while_proceeding_to_pay(self):
        soup=self.util.beautiful_soup(self.driver.page_source)
        uk_notify=soup.find(
            "div", class_="uk-notify uk-notify-top-center")
        if str(uk_notify) != "None":
            assert False, ("Not able to proceed for payment. Please check for error message")
        else:
            pass