@wip
Feature: WebPages
 Test Create, Edit and Delete WebPages


 Scenario: Create a new Webpage and publish
    Given Go to WebPages
    And Click on Create New Webpage
    Then Enter the details and click on save & publish
    Then Verify if Webpage is saved in BO successfully
    And Verify if webpage is published in marketplace successfully

Scenario: Create a new Webpage and save as draft
    Given Go to WebPages
    And Click on Create New Webpage
    Then Enter the details and click on save as draft
    Then Verify if Webpage is saved in BO successfully
    And Verify if webpage is  not published in marketplace

Scenario: Edit an existing webpage and save the changes
    Given Click on any existing webpage
    Then Edit the details and click on save & publish
    Then Verify if changes are saved successfully BO
    And Verify if changes are reflecting in marketplace successfully
