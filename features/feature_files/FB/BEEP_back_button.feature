Feature: When & where to show the back button on Menu page
  #@beep.delivery
  Scenario: Open store with Source: beepit, OrderType: delivery, Pre-order enabled: True
    Given Navigate to scan homepage
    And Select delivery to location and store, choose Food delivery
    When Verify the Visibility of bar is true and position of back button is in DELIVER TO bar, click the back button
    Then Take back to homepage

  #@beep.delivery
  Scenario: Open store with Source: beepit, OrderType: delivery, Pre-order enabled: False
    Given Navigate to scan homepage
    And Select delivery to location and store which without preorder, choose Food delivery
    When Verify the Visibility of bar is true and position of back button is in DELIVER TO bar, click the back button
    Then Take back to homepage

  #@beep.delivery
  Scenario: Open store with Source: beepit, OrderType: pickup, Pre-order enabled: True
    Given Navigate to scan homepage
    And Select delivery to location and store, choose Self pickup
    When Verify the Visibility of bar is true and position of back button is in DELIVER TO bar, click the back button
    Then Take back to homepage

  #@beep.delivery
  Scenario: Open store with Source: beepit, OrderType: pickup, Pre-order enabled: False
    Given Navigate to scan homepage
    And Select delivery to location and store which without preorder, choose Self pickup
    When Verify the Visibility of bar is false and position of back button is in STORE NAME bar, click the back button
    Then Take back to homepage

  #@beep.delivery
  Scenario: Open store with Source: store URL, OrderType: delivery, Pre-order enabled: True
    Given Navigate to a store and choose Food delivery
    Then Verify the Visibility of bar is true and no back button on current page

  #@beep.delivery
  Scenario: Open store with Source: store URL, OrderType: delivery, Pre-order enabled: False
    Given Navigate to a store which without preorder and choose Food delivery
    Then Verify the Visibility of bar is true and no back button on current page