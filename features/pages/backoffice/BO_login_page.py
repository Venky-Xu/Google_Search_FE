from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from features.pages.backoffice.BO_locators import Locator
from util.commonfunctions import Actions
import os
from util.util import Util
from hamcrest import assert_that


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        Actions(self.driver).navigate_to_url(Util.BO_LOGIN_URL)

    def login_into_bo(self, username, password):
        Actions(self.driver).send_keys(Locator.login_username, username)
        Actions(self.driver).send_keys(Locator.login_password, password)
        Actions(self.driver).common_click(Locator.login_button)

    def verify_login(self):
        Actions(self.driver).explicit_wait(["element_located"], 10, Locator.verify_login)
        assert_that("Dashboard - StoreHub Backoffice", self.driver.title, "Login is unsuccessful")