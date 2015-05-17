Feature: Solve cryptarithmetic puzzle
  Program should solve cryptarithmetic puzzle and returns result to user

  Scenario: Program execution
    When I run the program with argument "ODD + ODD == EVEN"
    Then I see a result of "655 + 655 == 1310\n855 + 855 == 1710"
