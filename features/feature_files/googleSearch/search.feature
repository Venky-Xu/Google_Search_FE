 @smoke
 @Chrome
 Feature: Google Search
 Test search feature in Google page

  Scenario: automatic matching keyword
    Given I am on google page
    When fill in search box with keyword "wiki"
    Then Verify the automatic matching results
    And select the first result in the dropdown list
    Then Verify the direct is work

  Scenario: search basic flow + Enter
    Given I am on google page
    When fill in search box with keyword "wiki"
    And finish with Enter
    Then Verify the searched results are correct

  Scenario: search basic flow + search button
    Given I am on google page
    When fill in search box with keyword "wiki"
    And click the search button
    Then Verify the searched results are correct