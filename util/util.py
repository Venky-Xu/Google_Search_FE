from bs4 import BeautifulSoup
import csv
import random
import time
import requests
import os
from dotenv import load_dotenv
import json
from datetime import datetime
import uuid


class Util:

    load_dotenv()
    p = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
    ANDROID_BASE_CAPS = {
        'automationName': 'UIAutomator2',
        'platformName': 'Android',
        'app': p+'/app/StoreHub_Fat_1.7.5_202002231708.apk',
        'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION'),
        'deviceName': os.getenv('ANDROID_DEVICE_NAME'),
        'noReset': bool(os.getenv('ANDROID_NORESET')),
        'appActivity': os.getenv('ANDROID_APP_ACTIVITY'),
        'appPackage': os.getenv('ANDROID_APP_PACKAGE'),
        "autoLaunch": bool(os.getenv('ANDROID_AUTO_LAUNCH')),
        'newCommandTimeout': int(os.getenv('ANDROID_NEW_COMMAND_TIMEOUT'))
    }
    EXECUTOR = 'http://127.0.0.1:4723/wd/hub'
    URL = os.getenv('BEEP_URL')
    BEEP_URL = os.getenv('BEEP_URL')
    BEEP_DELIVERY_URL = os.getenv('BEEP_DELIVERY_URL')
    CLAIM_URL = os.getenv('CLAIM_URL')
    BEEP_PHONE_NUMBER = os.getenv('PHONE_NUMBER')
    MVP_BEEP_DELIVERY_URL = os.getenv('MVP_BEEP_DELIVERY_URL')
    BO_LOGIN_URL = os.getenv('BO_LOGIN_URL')
    BO_LOGIN_USERNAME = os.getenv('LOGIN_USERNAME')
    BO_LOGIN_PASSWORD = os.getenv('LOGIN_PASSWORD')
    SIGNUP_URL = os.getenv('SIGNUP_URL')
    SIGNUP_STEP_2_URL = os.getenv("SIGNUP_STEP_2_URL")
            
    def test_data(self):
        with open("./util/json/testData.json", 'r') as load_b:
            test_data = json.load(load_b)
            test_data["username"] = "divya.singla+" + str(random.randint(500,100000)) + "@storehub.com"
            test_data["business_name"] = "cafe"+ str(random.randint(500,100000))
            test_data["product_name"] = "Test"+ str(random.randint(500,100000))
            test_data["sku"] = "test"+ str(random.randint(500,100000))
            return test_data
            
    def beautiful_soup(self, page_source):
        soup = BeautifulSoup(page_source, "html.parser")
        return soup

    @staticmethod
    def get_datetime():
        return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    @staticmethod
    def create_receipt_number():
        return "001" + datetime.now().strftime("%y%m%d%H%M%S") + str(random.randint(1, 9))

    @staticmethod
    def uuid_32():
        uuid32 = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid1())))
        return uuid32


class Interface:
    def __init__(self):
        self.current_time = Util.get_datetime()
        self.receipt_number = Util.create_receipt_number()
        self.transaction_id = Util.uuid_32()

    def add_transaction_sale(self):
        with open("./util/json/transactionRecordswithSale.json", 'r') as load_b:
            transaction = json.load(load_b)
            transaction["createdTime"] = self.current_time
            transaction["receiptNumber"] = self.receipt_number
            transaction["transactionId"] = self.transaction_id
        with open("./util/json/mobileAPIHeader.json", 'r') as load_h:
            headers = json.load(load_h)
        url = os.getenv('API_URL')
        body = json.dumps(transaction)
        response = requests.post(url, data=body, headers=headers)
        return response.text

    def add_transaction_cancel(self):
        with open("./util/json/transactionRecordswithCancel.json", 'r') as load_b:
            transaction = json.load(load_b)
            transaction["createdTime"] = self.current_time
            transaction["receiptNumber"] = self.receipt_number
            transaction["transactionId"] = self.transaction_id
            transaction["cancelledAt"] = self.current_time
            transaction["modifiedTime"] = self.current_time
        with open("./util/json/mobileAPIHeader.json", 'r') as load_h:
            headers = json.load(load_h)
        url = os.getenv('API_URL')
        body = json.dumps(transaction)
        response = requests.post(url, data=body, headers=headers)
        return response.text
