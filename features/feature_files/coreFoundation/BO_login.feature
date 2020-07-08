 @smoke
 @Chrome
 @CF
 Feature: LoginTest
 Want to login in BO-Back office

  Scenario: Login with valid credentials
    Given I am on Login page
    When Logging into backoffice with valid credentials username and password
    Then It logged in successfully
