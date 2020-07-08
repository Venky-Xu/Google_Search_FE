Feature: claim
  @fixture.platform.chrome
  Scenario: Basic Claim
    Given Transfer to order paid
    When check view receipt
    Then check balance
