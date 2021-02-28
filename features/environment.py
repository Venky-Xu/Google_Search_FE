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


@fixture
def init_safari_driver_mobile_emulation_beep_delivery(context, timeout=30, **kwargs):
    context.safari_driver = webdriver.Safari()
    context.safari_driver.get(Util.BEEP_DELIVERY_URL)
    context.safari_driver.maximize_window()
    context.safari_driver.implicitly_wait(20)
    return context.safari_driver


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
    elif tag == 'fixture.platform.safari':
        context.chrome_driver = use_fixture(init_safari_driver_mobile_emulation_beep_delivery, context, timeout=10)


def before_scenario(context, scenario):
    if context.platform == Platform.Chrome.value and context.pu == ProductUnits.CoreFoundation.value:
        context.chrome_driver = use_fixture(init_chrome_driver, context, timeout=10)


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








