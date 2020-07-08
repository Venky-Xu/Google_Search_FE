from features.pages.backoffice.BO_login_page import LoginPage
from behave import *
from selenium import webdriver
import os


@given(u'I am on Login page')
def navigate_to_bo(context):
     context.login = LoginPage(context.chrome_driver)


@when(u'Logging into backoffice with valid credentials username and password')
def valid_credentials(context):
     context.login.login_into_bo(os.getenv("LOGIN_USERNAME"),os.getenv("LOGIN_PASSWORD"))


@then(u'It logged in successfully')
def verify_login_successful(context):
     context.login.verify_login()
