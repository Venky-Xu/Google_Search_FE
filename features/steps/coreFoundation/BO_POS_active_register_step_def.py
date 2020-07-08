from behave import *
from features.pages.backoffice.BO_login_page import LoginPage
from features.pages.backoffice.BO_index_page import Index
from features.pages.backoffice.BO_ipad_register_page import Register
from features.pages.pos.POS_active_register_page import ActiveRegister
import os
import time


@given(u'I already logged in BO')
def step_impl(context):
    context.login = LoginPage(context.chrome_driver)
    context.login.login_into_bo(os.getenv("LOGIN_USERNAME"), os.getenv("LOGIN_PASSWORD"))
    context.login.verify_login()


@step(u'Negative to iPad Registers page')
def step_impl(context):
    time.sleep(50)
    context.registerMenu = Index(context.chrome_driver)
    context.registerMenu.negative_ipad_register()


@when(u'Click Add iPad Register and click Yes on Confirm dialog')
def step_impl(context):
    context.register = Register(context.chrome_driver)
    context.register.verify_page()
    context.register.add_ipad_register()


@when(u'Click Save on Add iPad Register page')
def step_impl(context):
    context.register.save_register()


@then(u'Negative to Active Register page on POS')
def step_impl(context):
    context.active = ActiveRegister(context.android_driver)
    context.platform = 'Android'
    context.active.switch_to_active_page()


@step(u'Input name of merchant, email and password, then click Continue')
def step_impl(context):
    context.active.input_info('angdo', os.getenv("LOGIN_USERNAME"), os.getenv("LOGIN_PASSWORD"))
    context.active.click_continue()


@then(u'transfer to PIN code page')
def step_impl(context):
    context.active.verify_login_page()
