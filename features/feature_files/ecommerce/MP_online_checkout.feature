@marketplace
Feature: MarketplaceCheckoutTest
 Testing checkout scenarios in marketplace

Background: User is logged in
    Given I am on Login page
    When Logging into backoffice with valid credentials username and password
    Then It logged in successfully

Scenario: Place a delivery order online and checkout successfully
    Given Store is already online and published
    Then Add a product in BO
    And Sell a product online and add to feature product list
    Then Go to marketplace and verify if product is online or not
    Then Click on product and verify product details like price, name and variants
    And Verify product stock status whether In stock or not
    Then Click on Add to cart
    And Verify product details in checkout pop and click on checkout
    Then Verify if user is directed to Checkout-Step 1 process
    And Click on Login and login using customer's login credentials
    Then Verify that user is logged in successfully and Contact Info should be autofilled.
    And Click on continue button to direct to Checkout-Step 2 process
    Then Verify if successfully directed to checkout-step 2
    Then Select Delivery fulfillment method
    And Add shipping address and click on save
    Then Select shipping zone
    And Verify if shipping fee is added to product price in Cart Summary
    Then Click on Proceed to pay for Delivery
    And Verify if it is directed to Payment page
    Then Enter all payment details and Proceed
    Then Verify if payment is made and order is placed successfully
    And Verify delivery order details in order confirmation page

Scenario: Place a pickup order online and checkout successfully
    Given Store is already online and published
    Then Add a product in BO
    And Sell a product online and add to feature product list
    Then Go to marketplace and verify if product is online or not
    Then Click on product and verify product details like price, name and variants
    And Verify product stock status whether In stock or not
    Then Click on Add to cart
    And Verify product details in checkout pop and click on checkout
    Then Verify if user is directed to Checkout-Step 1 process
    And Click on Login and login using customer's login credentials
    Then Verify that user is logged in successfully and Contact Info should be autofilled.
    And Click on continue button to direct to Checkout-Step 2 process
    Then Verify if successfully directed to checkout-step 2
    Then Select Pickup fulfillment method
    And Check availability of items in Pickup Store and select it
    Then Click on Proceed to pay for Pickup
    And Verify if it is directed to Payment page
    Then Enter all payment details and Proceed
    Then Verify if payment is made and order is placed successfully
    And Verify pickup order details in order confirmation page
    