Feature: Solve zebra puzzle
  Program should solve zebra puzzle and returns result to user

  Scenario: Program execution
    When I run the zebra program
    Then I see a result of "Norwegian drinks water, Japanese owns the zebra"
