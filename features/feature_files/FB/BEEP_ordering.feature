Feature: Ordering flow
  @fixture.platform.chrome
  @smoke
  @FB
  @beep
  Scenario: Basic Order
    Given Navigate to a store
    When Add an item to cart and checkout
    Then  payment


