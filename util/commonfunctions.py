from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Actions(object):
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def safari_click(self, xpath):
        self.driver.execute_script('arguments[0].click();', self.driver.find_element(By.XPATH, xpath))

    def common_click(self, xpath):
        elem = self.driver.find_element(By.XPATH, xpath)
        elem.click()

    def get_text(self, xpath):
        elem = self.driver.find_element(By.XPATH, xpath)
        return elem.text

    def send_keys(self, xpath, keys):
        elem = self.driver.find_element(By.XPATH, xpath)
        elem.send_keys(keys)

    def input_clear(self, xpath):
        elem = self.driver.find_element(By.XPATH, xpath)
        elem.clear()
        return elem

    def get_current_url(self):
        current_page_url = self.driver.current_url
        return current_page_url

    def get_element(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element

    def get_element_lists(self, xpath):
        element_list = self.driver.find_elements(By.XPATH, xpath)
        return element_list

    def get_single_object_from_list(self, xpath, index):
        element_list = self.driver.find_elements(By.XPATH, xpath)
        return element_list[index - 1]

    def switch_to_iframe_elem(self, index):
        iframe = self.driver.find_elements(By.TAG_NAME, "iframe")[index]
        self.driver.switch_to.frame(iframe)

    def switch_to_content(self):
        self.driver.switch_to.default_content()

    def explicit_wait(self, conditions, time, xpath):
        for condition in conditions:
            if condition == "element_located":
                element = WebDriverWait(self.driver, time).until(ec.presence_of_element_located((By.XPATH, xpath)))
            elif condition == "element_clickable":
                element = WebDriverWait(self.driver, time).until(ec.element_to_be_clickable((By.XPATH, xpath)))
            elif condition == "element_invisibility":
                element = WebDriverWait(self.driver, time).until(ec.invisibility_of_element_located((By.XPATH, xpath)))
            elif condition =="element_visibility":
                element = WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((By.XPATH, xpath)))
        return element
    
    def choose_item_from_dropdown(self, condition, locator, data):
        if condition == "visible_text":
            Select(self.get_element(locator)).select_by_visible_text(data)
        elif condition == "value":
            Select(self.get_element(locator)).select_by_value(data)
        elif condition == "index":
            Select(self.get_element(locator)).select_by_index(data)
        
       
    def add_cookies(self):
        self.driver.add_cookie({'name': '__cid', 'value': '5e7f598cd24675f3fbac3a4d'})
        self.driver.add_cookie({'name': 'sid',
                                          'value': 's%3AjQl3Hw2FpkpGaVdbeDOdu3AXi6Hp_c-h.ngIYw3kp4tAWmkWn9kD8csGBMHA%2BRUPQJhjLRHpQ9M8'})

        self.driver.add_cookie(
            {'name': '__h', 'value': 'U2FsdGVkX188AzbXuu9%2B2NS3VJESYjJnJINpM0I5brLvWKVlPIQA5wYVhAOKTBFr'})
        self.driver.add_cookie({'name': '__s', 'value': '5e8dab9e52c38c00064080b3'})

    def set_local_storage(self, key, value):
        self.driver.execute_script('window.localStorage.setItem(arguments[0], arguments[1]);', key, value)

    def get_local_storage(self, key):
        self.driver.execute_script('return window.localStorage.getItem(arguments[0]);', key)  
        
    def navigate_to_bo_menu_item(self, menu_item_name):
        self.driver.find_element(By.XPATH, "//a[contains(.,'"+menu_item_name+"')]").click()
    
    def send_keys_from_keyboard(self, xpath, keys, non_text_keys):
        if non_text_keys == "ENTER":
            self.driver.find_element(By.XPATH, xpath).send_keys(keys, Keys.ENTER)
            
    def get_attribute(self, xpath, attribute_name):
        value = self.driver.find_element(By.XPATH, xpath).get_attribute(attribute_name)
        return value
