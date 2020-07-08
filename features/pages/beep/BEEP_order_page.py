from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import selenium
import time
from util.commonfunctions import Actions


class Order(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def verify_visibility_of_bar(self):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, Locator.bar)))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def verify_visibility_of_back(self):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, Locator.edit)))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def verify_back_is_in_deliver_or_pickup_bar(self):
        grandparent_of_summary_bar = self.driver.find_element(By.XPATH, Locator.bar+'/../..')
        parent_of_back = self.driver.find_element(By.XPATH, Locator.back+'/..')
        if grandparent_of_summary_bar == parent_of_back:
            return True
        else:
            return False

    def verify_back_is_in_store_name_bar(self):
        grandparent_of_summary_bar = self.driver.find_element(By.XPATH, Locator.store_name+'/../..')
        parent_of_back = self.driver.find_element(By.XPATH, Locator.back_in_store_name+'/..')
        if grandparent_of_summary_bar == parent_of_back:
            return True
        else:
            return False

    def click_back_button(self):
        self.driver.find_element(By.XPATH, Locator.back).click()

    def click_back_button_in_store_name(self):
        self.driver.find_element(By.XPATH, Locator.back_in_store_name).click()

    def legal_drinking_age(self):
        try:
            time.sleep(5)
            Actions(self.driver).explicit_wait(["element_clickable"], 20, Locator.yes_i_am)
            Actions(self.driver).common_click(Locator.yes_i_am)
        except selenium.common.exceptions.TimeoutException:
            pass

    def clear_shopping_cart(self):
        time.sleep(2)
        Actions(self.driver).explicit_wait(["element_located"], 20, Locator.cart_label_number)
        count_in_cart = Actions(self.driver).get_text(Locator.cart_label_number)
        # print(count_in_cart)
        if int(count_in_cart) != 0:
            Actions(self.driver).common_click(Locator.cart_label_number)
            Actions(self.driver).explicit_wait(["element_clickable"], 10, Locator.clear_all)
            time.sleep(2)
            Actions(self.driver).common_click(Locator.clear_all)
            time.sleep(1)
            Actions(self.driver).common_click(Locator.cart_label_number)
        else:
            pass

    def clear_shopping_cart_safari(self):
        time.sleep(4)
        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, Locator.cart_label_number)))
        count_in_cart = self.driver.find_element(By.XPATH, Locator.cart_label_number).text
        print(count_in_cart)
        if int(count_in_cart) != 0:
            Actions.safari_click(self, Locator.cart_label_number)
            WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, Locator.clear_all)))
            time.sleep(2)
            Actions.safari_click(self, Locator.clear_all)
            time.sleep(1)
            Actions.safari_click(self, Locator.item_list)
        else:
            pass

    def add_item_into_cart(self):
        Actions(self.driver).explicit_wait(["element_located"], 10, Locator.order_now)
        time.sleep(2)
        Actions(self.driver).get_single_object_from_list(Locator.items_increase, 1).click()
        time.sleep(2)
        try:
            Actions(self.driver).explicit_wait(["element_clickable"], 10, Locator.OK)
            size = Actions(self.driver).get_single_object_from_list(Locator.item_simple_selection, 2).text
            Actions(self.driver).get_single_object_from_list(Locator.item_simple_selection, 2).click()
            time.sleep(1)
            add_ons = Actions(self.driver).get_text(Locator.item_multiple_selection)
            Actions(self.driver).common_click(Locator.item_multiple_selection)
            # add_ons = self.driver.find_element(By.XPATH, Locator.item_multiple_selection).text
            # self.driver.find_element(By.XPATH, Locator.item_multiple_selection).click()
            time.sleep(1)
            summary = Actions(self.driver).get_text(Locator.item_detail_summary)
            time.sleep(2)
            assert summary == size+', '+add_ons
            time.sleep(2)
            # Actions(self.driver).get_single_object_from_list(Locator.items_increase, 0).click()
            Actions(self.driver).common_click(Locator.item_detail_add)
            time.sleep(2)
            # Actions(self.driver).get_single_object_from_list(Locator.items_increase, 0).click()
            Actions(self.driver).common_click(Locator.item_detail_add)
            time.sleep(3)
            item_detail = Actions(self.driver).get_single_object_from_list(Locator.item_detail, 0)
            single_price = Actions(item_detail).get_text('span')
            quantity = Actions(self.driver).get_text(Locator.item_detail_quantity)
            order_info = {'single_price': single_price, 'quantity': quantity}
            Actions(self.driver).common_click(Locator.OK)
            time.sleep(5)
            return order_info
        except selenium.common.exceptions.TimeoutException:
            single_price = Actions(Actions(self.driver).get_element(Locator.item_detail)).get_text('span')
            quantity = Actions(self.driver).get_text(Locator.item_detail_quantity)
            order_info = {'single_price': single_price, 'quantity': quantity}
            return order_info

    def add_item_into_cart_safari(self):
        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, Locator.order_now)))
        Actions.safari_click(self, Locator.first_item_add)
        time.sleep(1)
        try:
            WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, Locator.OK)))
            size = self.driver.find_element(By.XPATH, Locator.item_simple_selection).text
            Actions.safari_click(self, Locator.item_simple_selection)
            time.sleep(1)
            add_ons = self.driver.find_element(By.XPATH, Locator.item_multiple_selection).text
            Actions.safari_click(self, Locator.item_multiple_selection)
            time.sleep(1)
            summary = self.driver.find_element(By.XPATH, Locator.item_summary).text
            assert summary == size+', '+add_ons
            Actions.safari_click(self, Locator.item_detail_add)
            time.sleep(2)
            Actions.safari_click(self, Locator.item_detail_add)
            time.sleep(3)
            single_price = self.driver.find_element(By.XPATH, Locator.item_detail_single_price).text
            single_price1 = single_price[2:]
            quantity = self.driver.find_element(By.XPATH, Locator.item_detail_quantity).text
            order_info = {'single_price': single_price1, 'quantity': quantity}
            Actions.safari_click(self, Locator.OK)
            time.sleep(2)
            return order_info
        except selenium.common.exceptions.TimeoutException:
            single_price = self.driver.find_element(By.XPATH, Locator.first_item_single_price).text
            quantity = self.driver.find_element(By.XPATH, Locator.first_item_quantity).text
            order_info = {'single_price': single_price, 'quantity': quantity}
            return order_info

    def verify_items_in_cart(self, count):
        count_in_cart = Actions(self.driver).get_text(Locator.cart_label_number)
        assert count == int(count_in_cart)

    def checkout_and_pay(self):
        Actions(self.driver).common_click(Locator.order_now)
        time.sleep(2)
        self.driver.implicitly_wait(10)
        Actions(self.driver).explicit_wait(["element_located"], 20, Locator.login)
        subtotal = Actions(self.driver).get_single_object_from_list(Locator.money, 2).text.split(' ')[1]
        total = Actions(self.driver).get_single_object_from_list(Locator.money, 0).text.split(' ')[1]
        total_info = {'subtotal': subtotal, 'total': total}
        time.sleep(2)
        Actions(self.driver).common_click(Locator.Pay)
        self.driver.implicitly_wait(10)
        return total_info

    def checkout(self):
        Actions(self.driver).common_click(Locator.order_now)
        self.driver.implicitly_wait(10)

    def pay(self):
        Actions(self.driver).explicit_wait(["element_located"], 20, Locator.login)
        subtotal = Actions(self.driver).get_single_object_from_list(Locator.money, 2).text.split(' ')[1]
        total = Actions(self.driver).get_single_object_from_list(Locator.money, 0).text.split(' ')[1]
        total_info = {'subtotal': subtotal, 'total': total}
        time.sleep(2)
        Actions(self.driver).common_click(Locator.Pay)
        self.driver.implicitly_wait(10)
        return total_info

    def checkout_and_pay_safari(self):
        Actions.safari_click(self, Locator.order_now)
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, Locator.subtotal)))
        subtotal = self.driver.find_element(By.XPATH, Locator.subtotal).text[2:]
        total = self.driver.find_element(By.XPATH, Locator.total).text
        total_info = {'subtotal': subtotal, 'total': total}
        time.sleep(2)
        Actions.safari_click(self, Locator.Pay)
        self.driver.implicitly_wait(10)
        return total_info








