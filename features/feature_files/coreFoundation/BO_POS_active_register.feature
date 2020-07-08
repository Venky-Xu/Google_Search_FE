

Feature: iPad registers
  @fixture.platform.all
  Scenario: Add iPad registers on BO side and active register on POS
    Given I already logged in BO
    And Negative to iPad Registers page
    When Click Add iPad Register and click Yes on Confirm dialog
    And Click Save on Add iPad Register page
    Then Negative to Active Register page on POS
    And Input name of merchant, email and password, then click Continue
    Then transfer to PIN code page
