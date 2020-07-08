from features.pages.pos.POS_locators import Locator
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait


class ActiveRegister(object):
    def __init__(self, driver):
        self.driver = driver
#transfer to appium
    def switch_to_active_page(self):
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("%s")' % Locator.text_active_register).click()

    def input_info(self, store_name, email, password):
        WebDriverWait(self.driver, 1).until(
            lambda x: x.find_element(MobileBy.ACCESSIBILITY_ID, Locator.accessibility_id_store_name))
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, Locator.accessibility_id_store_name).send_keys(store_name)
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, Locator.accessibility_id_activation_email).send_keys(email)
        self.driver.find_element(
            MobileBy.ACCESSIBILITY_ID, Locator.accessibility_id_activation_password).send_keys(password)

    def click_continue(self):
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("%s")' % Locator.text_continue).click()

    def verify_login_page(self):
        self.driver.find_element(MobileBy.ID, Locator.id_Allow).click()


