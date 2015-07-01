# -*- coding: utf-8 -*-

Feature: Create a new list
  As a python QAloper
  I would like to create new lists
  So that I can manage and use them in my scripts


  Background:
    Given a configured python environment


  @test1
  Scenario: Create new empty list
    When  I create a new empty list
    Then  the list is created
    And   the length of the list is "0"


  @test2
  Scenario: Create a new list with some values
    When  I create a new list with values "qa,test,behave"
    Then  the list is created
    And   the length of the list is "3"
    And   the list has got next content:
            | position | content |
            | 0        | qa      |
            | 1        | test    |
            | 2        | behave  |


  @test3 @nok
  Scenario: Create a new list with some values
    When  I create a new list with values "qa,test,behave"
    Then  the list is created
    And   the length of the list is "2"
    And   the list has got next content:
            | position | content |
            | 0        | qa      |
            | 1        | test    |
            | 2        | behave  |
