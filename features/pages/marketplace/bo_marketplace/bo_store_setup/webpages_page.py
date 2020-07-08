from selenium import webdriver
from pages.backoffice.bo_locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from util.util import *
import time

class WebPages(object):

    def __init__(self, driver):
        self.driver = driver