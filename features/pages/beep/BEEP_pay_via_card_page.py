from features.pages.beep.BEEP_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
from util.commonfunctions import Actions


class Card(object):
    def __init__(self, driver):
        self.driver = driver

    def card_information_input(self, card_number, valid_date, cvv, name_on_card):

        Actions(self.driver).presence_of_element_located(10, Locator.name_on_card)
        Actions(self.driver).send_keys(Locator.name_on_card, name_on_card)
        time.sleep(10)
        Actions(self.driver).switch_to_iframe_elem(0)

        time.sleep(2)
        print(self.driver.find_element_by_xpath('//span').text)
        Actions(self.driver).send_keys(Locator.card_number, card_number)
        Actions(self.driver).switch_to_content()
        Actions(self.driver).switch_to_iframe_elem(1)
        time.sleep(2)
        Actions(self.driver).send_keys(Locator.valid_date, valid_date)
        Actions(self.driver).switch_to_content()
        Actions(self.driver).switch_to_iframe_elem(2)
        time.sleep(2)
        Actions(self.driver).send_keys(Locator.cvv, cvv)
        Actions(self.driver).switch_to_content()
        time.sleep(5)
        Actions(self.driver).common_click(Locator.pay_money)

    def card_information_input_safari(self, card_number, valid_date, cvv, name_on_card):

        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, Locator.card_number)))
        self.driver.find_element(By.XPATH, Locator.card_number).send_keys(card_number)
        self.driver.find_element(By.XPATH, Locator.valid_date).send_keys(valid_date)
        self.driver.find_element(By.XPATH, Locator.cvv).send_keys(cvv)
        self.driver.find_element(By.XPATH, Locator.name_on_card).send_keys(name_on_card)
        time.sleep(2)
        Actions.safari_click(self, Locator.pay_money)
