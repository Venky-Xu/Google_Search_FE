from features.pages.google.Google_locators import Locator
from util.commonfunctions import Actions
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.keys import Keys


class Search(object):
    def __init__(self, driver):
        self.driver = driver
        Actions(self.driver).navigate_to_url("https://www.google.co.nz")

    def input_keyword(self, keyword):
        Actions(self.driver).explicit_wait("element_located", 10, Locator.search_box)
        Actions(self.driver).input_clear(Locator.search_box)
        Actions(self.driver).send_keys(Locator.search_box, keyword)

    def get_automatic_matching(self):
        Actions(self.driver).explicit_wait("element_located", 10, Locator.matching)
        return Actions(self.driver).get_texts(Locator.matching)

    def send_enter(self):
        Actions(self.driver).send_keys(Locator.search_box, Keys.ENTER)

    def select_the_first_result_of_dropdown(self):
        Actions(self.driver).common_click('//li[@class="sbct"][1]')

    def click_search(self):
        Actions(self.driver).common_click(Locator.search_button)