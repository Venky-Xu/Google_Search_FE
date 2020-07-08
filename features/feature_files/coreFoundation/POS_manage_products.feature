@fixture.browser.android
Feature: menu-enter: Manage products

  Scenario: Add, search and edit products
    Given Enter into menu drawer and click the manage products title
    When Add a product named "Juice" with price EX tax "10"
    And Search the added product via search condition
    Then This product should display successfully
    And Modify the name of the searched product form "Juice" to "Tea"
    Then Edit successfully
