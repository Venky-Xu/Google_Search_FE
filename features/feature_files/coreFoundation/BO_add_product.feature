@smoke
@CF
Feature: AddProduct
  Adding products in BO

  Scenario: Adding non tracking product in BO with variants
    Given I already logged in BO
    Then Go to Add products
    And Add a non tracking product with single and multiple choice Variants
    Then Verify product is saved successfully in BO


  Scenario: Adding simple tracking inventory product in BO with no variants
    Given I already logged in BO
    Then Go to Add products
    And Add simple tracking inventory product with no variants
    Then Verify product is saved successfully in BO

  Scenario: Adding simple tracking inventory product in BO with variants
    Given I already logged in BO
    Then Go to Add products
    And Add simple tracking inventory product with variants
    Then Verify product is saved successfully in BO

  Scenario: Adding a product with Variable price
    Given I already logged in BO
    Then Go to Add products
    And Add product with variable price
    Then Verify product is saved successfully in BO