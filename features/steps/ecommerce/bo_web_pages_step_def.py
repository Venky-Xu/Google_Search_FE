from pages.marketplace.bo_marketplace.bo_store_setup.webpages_page import WebPages
from behave import *
from selenium import webdriver
import os

@given(u'Go to WebPages')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Go to WebPages')


@step(u'Click on Create New Webpage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Click on Create New Webpage')


@then(u'Enter the details and click on save & publish')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Enter the details and click on save & publish')


@then(u'Verify if Webpage is saved in BO successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify if Webpage is saved in BO successfully')


@step(u'Verify if webpage is published in marketplace successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify if webpage is published in marketplace successfully')


@then(u'Enter the details and click on save as draft')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Enter the details and click on save as draft')


@step(u'Verify if webpage is  not published in marketplace')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify if webpage is  not published in marketplace')


@given(u'Click on any existing webpage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Click on any existing webpage')


@then(u'Edit the details and click on save & publish')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Edit the details and click on save & publish')


@then(u'Verify if changes are saved successfully BO')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify if changes are saved successfully BO')


@step(u'Verify if changes are reflecting in marketplace successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Verify if changes are reflecting in marketplace successfully')