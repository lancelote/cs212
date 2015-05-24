Feature: Solve floor puzzle
  Program should solve floor puzzle and returns result to user

  Scenario: Program execution
    When I run the floor program
    Then I see a result of "Hopper: 3, Kay: 2, Liskov: 4, Perlis: 5, Ritchie: 1"
