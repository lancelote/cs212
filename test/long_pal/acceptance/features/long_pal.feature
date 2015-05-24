Feature: Find the longest palindrome in the string
  Program should find the longest palindrome in the string

  Scenario Outline: Program execution
    When I run the long_pal program with "<argument>"
    Then I see a result of "<result>"
    Examples:
      | argument                  | result  |
      | racecar                   | (0, 7)  |
      | Racecar                   | (0, 7)  |
      | RacecarX                  | (0, 7)  |
      | Race carr                 | (7, 9)  |
      | something rac e car going | (8, 21) |
      | xxxxx                     | (0, 5)  |
      | Mad am I ma dam.          | (0, 15) |
