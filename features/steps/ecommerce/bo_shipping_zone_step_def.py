from pages.marketplace.bo_marketplace.bo_store_setup.shipping_zone_page import ShippingZone
from behave import *
from selenium import webdriver
import os

@given(u'Go to Shipping Zone page')
def step_impl(context):
    context.shippingzone = ShippingZone(context.driver)
    context.shippingzone.go_to_shipping_zone()

@step(u'Click on Add New Shipping Zone')
def step_impl(context):
    context.shippingzone.click_create_new_shipping_zone()


@then(u'Enter all local shipping details and click on save')
def step_impl(context):
    context.shipping_zone_id = context.shippingzone.enter_local_shipping_zone_details()


@then(u'Verify if Shipping Zone is added successfully in BO')
def step_impl(context):
    context.shippingzone.verify_new_shipping_zone_added_successfully(context.shipping_zone_id)


@then(u'Enter all International shipping details and click on save')
def step_impl(context):
    context.shipping_zone_id = context.shippingzone.enter_international_shipping_zone_details()

@given(u'There is an existing shipping zone')
def step_impl(context):
    context.shippingzone = ShippingZone(context.driver)
    context.existing_zone_id = context.shippingzone.check_for_existing_shipping_zone()


@then(u'Click on edit to edit existing shipping details')
def step_impl(context):
    context.shippingzone.click_on_edit_shipping_zone(context.existing_zone_id)


@step(u'Edit shipping details and save it')
def step_impl(context):
    context.shippingzone.edit_existing_shipping_zone()


@then(u'Verify if details have been edited successfully')
def step_impl(context):
    context.shippingzone.verify_edited_shipping_zone()


@then(u'Click on edit to delete existing shipping details')
def step_impl(context):
    context.shippingzone.click_on_edit_shipping_zone(context.existing_zone_id)


@then(u'Click on delete button')
def step_impl(context):
    context.shippingzone.delete_shipping_zone()


@step(u'Verify if shipping zone has been deleted successfully')
def step_impl(context):
    context.shippingzone.verify_deleted_shipping_zone(context.existing_zone_id)