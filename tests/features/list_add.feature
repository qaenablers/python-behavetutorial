# -*- coding: utf-8 -*-

Feature: ADD values in a list
  As a python QAloper
  I would like to manage the addition of values in lists
  So that I can create and use them


  @test4
  Scenario: ADD one value at the end of the list.
    Given a created empty list
    When  I add the value "123" at the end of the list
    Then  the length of the list is "1"
    And   the list has got next content:
            | position | content |
            | 0        | 123     |


  @test5
  Scenario Outline: ADD one value at the beginning of the list.
    Given a created empty list
    And   I add the value "<value1>" at the end of the list
    When  I add the value "<value2>" at the beginning of the list
    Then  the length of the list is "2"
    And   the list has got next content:
            | position | content  |
            | 0        | <value2> |
            | 1        | <value1> |

    Examples:
            | value1   | value2   |
            | 1234     | zzzz     |
            | ***qa*** | ...-,,,! |
            | be-have  | testing  |


  @test6 @nok
  Scenario Outline: ADD one value at the beginning of the list.
    Given a created empty list
    And   I add the value "<value1>" at the end of the list
    When  I add the value "<value2>" at the beginning of the list
    Then  the length of the list is "2"
    And   the list has got next content:
            | position | content  |
            | 0        | <value2> |
            | 1        | <value1> |

    Examples:
            | value1   | value2   |
            | 1234     | zzzz     |
            | ...-,,,! | ***qa*** |
            | be-have  | testing  |
