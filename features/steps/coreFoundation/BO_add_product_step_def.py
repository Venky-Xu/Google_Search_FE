from pages.backoffice.BO_product_page import Products
from pages.backoffice.BO_login_page import LoginPage
from behave import *
from selenium import webdriver
import os


@then(u'Go to Add products')
def step_impl(context):
    context.product = Products(context.chrome_driver)


@step(u'Add a non tracking product with single and multiple choice Variants')
def step_impl(context):
    context.product_id = context.product.add_product_with_variants_no_inventory()
 

@then(u'Verify product is saved successfully in BO')
def step_impl(context):
    context.product.verify_product_added_successfully(context.product_id)
    print("Verified successfully")
    
    
@step(u'Add simple tracking inventory product with no variants')
def step_impl(context):
    context.product_id = context.product.add_product_with_simple_inventory_no_variants()
   
   
@step(u'Add simple tracking inventory product with variants')
def step_impl(context):
    context.product_id = context.product.add_product_with_simple_inventory_and_variants()
    
@step(u'Add product with variable price')
def step_impl(context):
    context.product_id = context.product.add_variable_price_product()
   
   