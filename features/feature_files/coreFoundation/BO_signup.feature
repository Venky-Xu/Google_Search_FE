 @smoke
 @CF
 Feature: SignupTest
  Signing up new account in storehub

  Scenario: Signup-Signing up in storehub
    Given I am on signup page
    When Enter all details and click on sign up
    Then It should successfully direct to step two signup details page
    Then Enter all details in step two of signup process and click on next
    Then It should successfully logged in to Backoffice
    