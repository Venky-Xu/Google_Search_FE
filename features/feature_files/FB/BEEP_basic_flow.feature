Feature: Ordering and payment flow
  @fixture.platform.chrome
  @smoke
  @FB
  @beep.delivery
  Scenario: Merchant Self pickup
    Given Navigate to a store and choose Self pickup
    When Add an item into cart and fill pickup information
    Then payment process
  @fixture.platform.chrome
  @smoke
  @FB
  @beep.delivery
  Scenario: Merchant Food delivery
    Given Navigate to a store and choose Food delivery
    When Select delivery to address and add an item into cart
    Then payment process
  @fixture.platform.chrome
  @smoke
  @FB
  @beep.delivery
  Scenario: MVP Food delivery
    Given Navigate to scan homepage
    And Select delivery to location and store
    When Add an item into cart and fill delivery information
    #Then payment process

  @fixture.platform.chrome
  @smoke
  @FB
  @beep.delivery
  Scenario: MVP Self pickup
    Given Navigate to scan homepage
    And Select delivery to location and self pickup store
    When Add an item into cart and fill pickup information,
    #Then payment process

  @fixture.platform.safari
  @smoke
  @FB
  Scenario: Safari MVP Food delivery
    Given Navigate to scan homepage Safari Specially
    And Select delivery to location and store, choose Food delivery Safari Specially
    When Add an item into cart and fill delivery information Safari Specially
    Then payment process Safari Specially

  @fixture.platform.safari
  @smoke
  @FB
  Scenario: Safari MVP Self pickup
    Given Navigate to scan homepage Safari Specially
    And Select delivery to location and store, choose Self pickup Safari Specially
    When Add an item into cart and fill pickup information Safari Specially
    Then payment process Safari Specially