from features.pages.google.Google_locators import Locator
from util.commonfunctions import Actions


class Result(object):
    def __init__(self, driver):
        self.driver = driver

    def get_new_url(self):
        return Actions(self.driver).get_current_url()

    def get_keyword_results(self):
        return Actions(self.driver).get_texts(Locator.searched_results)