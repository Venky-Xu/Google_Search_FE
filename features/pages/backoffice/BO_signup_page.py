from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.backoffice.BO_locators import Locator
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from util.util import Util
from util.commonfunctions import Actions
import time
import os
from hamcrest import assert_that


class SignUp(object):

    def __init__(self, driver):
        self.driver = driver
        self.util = Util()
        self.data = self.util.test_data()

    def enter_details_and_signup(self):
        Actions(self.driver).send_keys(Locator.signup_email, self.data["username"])
        Actions(self.driver).send_keys(Locator.signup_password, self.data["password"])
        Actions(self.driver).choose_item_from_dropdown("visible_text", Locator.signup_country, self.data["country"])
        time.sleep(1)
        Actions(self.driver).common_click(Locator.signup_button)

    def verify_step_two_signup_page(self, step_2_url):
        self.step_two_signup_button = Actions(self.driver).explicit_wait(["element_located"], 10, Locator.step_two_signup_button)
        assert_that(self.driver.current_url, step_2_url, "It did not direct to step-2 signup details page successfully")
        
    def enter_step_two_signup_details(self):
        try:
            Actions(self.driver).send_keys(Locator.business_name, self.data["business_name"])
            Actions(self.driver).send_keys(Locator.firstname, self.data["first_name"])
            style = Actions(self.driver).get_attribute(Locator.capture_domain_frame, "style")
            if style == "":
                pass
            else:
                print(
                    "\nError------Unfortunately this domain is already taken. Click inside the field to make yours even more unique!\n")
                quit()
            Actions(self.driver).send_keys(Locator.lastname, self.data["last_name"])
            Actions(self.driver).send_keys(Locator.input_mobile_number, self.data["mobile_number"])
            Actions(self.driver).choose_item_from_dropdown("visible_text", Locator.input_business_type, self.data["business_type"])
            Actions(self.driver).choose_item_from_dropdown("visible_text", Locator.input_number_of_stores, self.data["number_of_stores"])
            time.sleep(1)
            self.step_two_signup_button.click()
        except NoSuchElementException as exception:
            print(exception)
            
    def verify_skip_tutorial(self):
        self.elementtext = Actions(self.driver).explicit_wait(["element_located"], 10, Locator.lets_go)
        assert_that(self.elementtext.text, "Let's go!", "Signup Unsuccessful" )

    def verify_successful_signup(self):
        self.verify_skip_tutorial()
