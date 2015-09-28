# -*- coding: utf-8 -*-

Feature: Create a new dict
  As a python QAloper
  I would like to create new dicts
  So that I can manage and use them in my scripts


  @test7
  Scenario: Create a new dict with one entry
    Given a configured python environment
    When  I create a new dict with key with this values:
            | key      | value   |
            | qa       | 12345   |
    Then  the dict is created
    And   the key "qa" has the value "12345"


  @test8
  Scenario Outline: Create a new dict with some values
    Given a configured python environment
    When  I create a new dict with key with this values:
            | key      | value   |
            | <key>    | <value> |
    Then  the dict is created
    And   the key "<key>" has the value "<value>"
    Examples:
            | key      | value  |
            | qa1      | 12345  |
            | qa2      | 67890  |

  @test9 @nok @specialtag
  Scenario: Create a new dict with one entry
    Given a configured python environment
    When  I create a new dict with key with this values:
            | key      | value   |
            | qa       | 12345   |
    Then  the dict is created
    And   the key "qa" has the value "11111111"