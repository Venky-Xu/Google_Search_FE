from selenium import webdriver
from appium import webdriver as AppiumDriver
import os
from util.util import Util
from util.platforms import Platform
from util.productUnits import ProductUnits
from behave.fixture import fixture, use_fixture
from selenium.webdriver.chrome.options import Options



@fixture
# Initialize Android driver
def init_android_driver(context, timeout=30, **kwargs):
    context.android_driver = AppiumDriver.Remote(
        command_executor=Util.EXECUTOR, desired_capabilities=Util.ANDROID_BASE_CAPS)
    return context.android_driver


@fixture
# Initialize Chrome driver and ignore security certification
def init_chrome_driver(context, timeout=30, **kwargs):
    options = webdriver.ChromeOptions()
    # ignore https SSL certificate, enter the login page directly
    options.add_argument('--ignore-certificate-errors')
    context.chrome_driver = webdriver.Chrome(chrome_options=options)
    context.chrome_driver.implicitly_wait(5)
    context.chrome_driver.maximize_window()
    return context.chrome_driver


# Change the geographic location of the browser
def set_location(context, latitude, longitude):
    context.chrome_driver.execute_script(
        "navigator.geolocation.getCurrentPosition = (s, e) => {s({coords: {latitude: " + str(latitude) + ",longitude: " + str(longitude) + "}});};")


# Initialization of Safari driver
@fixture
def init_safari_driver_mobile_emulation_beep_delivery(context, timeout=30, **kwargs):
    context.safari_driver = webdriver.Safari()
    context.safari_driver.get(Util.BEEP_DELIVERY_URL)
    context.safari_driver.maximize_window()
    context.safari_driver.implicitly_wait(20)
    return context.safari_driver


@fixture
def init_chrome_driver_mobile_emulation_beep_delivery(context, timeout=30, **kwargs):

    mobile_emulation = {

        "deviceMetrics": {"width": 411, "height": 731, "pixelRatio": 3.0},

        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
    # context.chrome_driver.get(Util.BEEP_DELIVERY_URL)
    # params = {
    #   "latitude": 3.1588266,
    #   "longitude": 101.7027275,
    #   "accuracy": 100
    # }
    # response = context.chrome_driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
    # context.chrome_driver.add_cookie({'name': '__cid', 'value': '5e7f598cd24675f3fbac3a4d'})
    # context.chrome_driver.add_cookie({'name': 'sid', 'value': 's%3AjQl3Hw2FpkpGaVdbeDOdu3AXi6Hp_c-h.ngIYw3kp4tAWmkWn9kD8csGBMHA%2BRUPQJhjLRHpQ9M8'})
    # context.chrome_driver.add_cookie({'name': '__h', 'value': 'U2FsdGVkX188AzbXuu9%2B2NS3VJESYjJnJINpM0I5brLvWKVlPIQA5wYVhAOKTBFr'})
    # context.chrome_driver.add_cookie({'name': '__s', 'value': '5e8dab9e52c38c00064080b3'})
    return context.chrome_driver


@fixture
def init_chrome_driver_mobile_emulation_beep(context, timeout=30, **kwargs):
    mobile_emulation = {'deviceName': 'iPhone 5'}
    options = webdriver.ChromeOptions()
    #options.add_experimental_option('prefs', {'intl.accept_languages': 'th'})
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    context.chrome_driver = webdriver.Chrome("./chromedriver", chrome_options=options)
    context.chrome_driver.get(Util.BEEP_URL)
    return context.chrome_driver


def before_tag(context, tag):
    if tag == 'fixture.platform.all':
        context.chrome_driver = use_fixture(init_chrome_driver, context, timeout=10)
        context.android_driver = use_fixture(init_android_driver, context, timeout=10)
        context.platform = Platform.All.value
    elif tag == 'CF':
        context.platform = Platform.Chrome.value
        context.pu = tag
    elif tag == 'beep.delivery':
        context.platform = Platform.Chrome.value
        context.pu = tag
    elif tag == 'beep':
        context.chrome_driver = use_fixture(init_chrome_driver_mobile_emulation_beep, context, timeout=10)
    elif tag == 'fixture.platform.safari':
        context.chrome_driver = use_fixture(init_safari_driver_mobile_emulation_beep_delivery, context, timeout=10)


def before_scenario(context, scenario):
    if context.platform == Platform.Chrome.value and context.pu == ProductUnits.CoreFoundation.value:
        context.chrome_driver = use_fixture(init_chrome_driver, context, timeout=10)
    elif context.platform == Platform.Chrome.value and context.pu == "beep.delivery":
        context.chrome_driver = use_fixture(init_chrome_driver_mobile_emulation_beep_delivery, context, timeout=10)

def after_scenario(context, scenario):
    if context.platform == Platform.Chrome.value:
        context.chrome_driver.quit()
        
'''
def after_step(context, step):
    if step.status == "failed":
        if not os.path.exists("output/failed_step_screenshots"):
            os.makedirs("output/failed_step_screenshots")
        if context.platform == Platform.Android:
            context.android_driver.save_screenshot("output/failed_step_screenshots/" + str(step.name) + "-failed.png")
        if context.platform == Platform.Chrome:
            context.chrome_driver.save_screenshot("output/failed_step_screenshots/" + str(step.name) + "-failed.png")
'''








