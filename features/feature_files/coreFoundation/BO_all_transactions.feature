 @Chrome
 @CF
 @smoke
 Feature: AllTransactions
  Scenario: Search a transaction via receipt number
    Given I already logged in BO
    And Navigate to All Transactions page
    When Input valid receipt number
    Then The corresponding transaction should appear in search result


  Scenario: Verify transaction detail page for a Sale
    Given I already logged in BO
    And Navigate to All Transactions page
    When click on a transaction with type: Sale
    Then the transaction detail page of the particular transaction should open with the correct details,Transaction Type: Sale


  Scenario: Verify transaction detail page for a Cancelled transaction
    Given I already logged in BO
    And Navigate to All Transactions page
    When click on a transaction with type: Cancelled
    Then Transaction Type in transaction details page should be "Cancelled", Cancel information should not be empty


