# -*- coding: utf-8 -*-

import behave
from behave import step
from hamcrest import assert_that, is_, equal_to, is_not

# Change the parameter matcher used in parsing step text: parse, cfparse, re
# https://pythonhosted.org/behave/api.html#step-parameters
behave.use_step_matcher("re")


#@given(u'a configured python environment')
@step(u'a configured python environment')
def configured_python_environment(context):
    assert_that(context.list, is_(None),
                "The list is not defined in Behave context")


#@when(u'I create a new empty list')
@step(u'I create a new empty list')
def create_an_empty_list(context):
    context.list = list()

#@when(u'I create a new list with values "(?P<values>.*)"')
@step(u'I create a new list with values "(?P<values>.*)"')
def create_new_list_with_values(context, values):
    array_values = values.split(",")
    context.list = list(array_values)


#@then(u'the list is created')
@step(u'the list is created')
def the_list_is_created(context):
    assert_that(isinstance(context.list, list), is_(True),
                "The list has not been created")


#@then(u'the length of the list is "(?P<length>\d*)"')
@step(u'the length of the list is "(?P<length>\d*)"')
def the_length_is(context, length):
    assert_that(len(context.list), is_(equal_to(int(length))),
                "The length is not the expected one")


#@then(u'the list has got next content')
@step(u'the list has got next content')
def the_list_has_got_content(context):
    for row in context.table:
        assert_that(context.list[int(row['position'])], is_(equal_to(row['content'])),
                    "The content is not the expected one")


#@given(u'a created empty list')
@step(u'a created empty list')
def a_created_list(context):
    context.execute_steps(u'''
         Given  a configured python environment
         When   I create a new empty list
         Then   the list is created
         And    the length of the list is "0"
    ''')
