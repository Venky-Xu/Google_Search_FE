from pages.backoffice.BO_signup_page import SignUp
from behave import *
from selenium import webdriver
import os
from util.commonfunctions import Actions
from util.util import Util

@given(u'I am on signup page')
def navigate_to_storehub_website(context):
    Actions(context.chrome_driver).navigate_to_url(Util.SIGNUP_URL)

@when(u'Enter all details and click on sign up')
def enter_details_and_signup(context):
    context.signup = SignUp(context.chrome_driver)
    context.signup.enter_details_and_signup()
    
@then(u'It should successfully direct to step two signup details page')
def verify_signup_details_page(context):
    context.signup.verify_step_two_signup_page(Util.SIGNUP_STEP_2_URL)

@then(u'Enter all details in step two of signup process and click on next')
def enter_step_two_signup_details(context):
    context.signup.enter_step_two_signup_details()

@then(u'It should successfully logged in to Backoffice')
def verify_successful_signup(context):
    context.signup.verify_successful_signup()




