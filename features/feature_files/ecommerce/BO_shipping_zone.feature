@smoke
Feature: ShippingZone
 Add, Edit and Delete Local and International Shipping Zone scenarios

Background: User is logged in
    Given I am on Login page
    When Logging into backoffice with valid credentials username and password
    Then It logged in successfully

 Scenario: Adding a new online local shipping zone in BO
    Given Go to Shipping Zone page
    And Click on Add New Shipping Zone
    Then Enter all local shipping details and click on save
    Then Verify if Shipping Zone is added successfully in BO

 Scenario: Adding a new online International shipping zone in BO
    Given Go to Shipping Zone page
    And Click on Add New Shipping Zone
    Then Enter all International shipping details and click on save
    Then Verify if Shipping Zone is added successfully in BO

 Scenario: Edit existing shipping zone and save it
   Given There is an existing shipping zone
   Then Click on edit to edit existing shipping details
   And Edit shipping details and save it
   Then Verify if details have been edited successfully

 Scenario: Delete an existing shipping zone
   Given There is an existing shipping zone
   Then Click on edit to delete existing shipping details
   Then Click on delete button
   And Verify if shipping zone has been deleted successfully
