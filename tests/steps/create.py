# -*- coding: utf-8 -*-

import behave
from behave import step
from hamcrest import assert_that, is_, equal_to, is_not, is_in
import logging

# Change the parameter matcher used in parsing step text: parse, cfparse, re
# https://pythonhosted.org/behave/api.html#step-parameters
behave.use_step_matcher("re")

__logger__ = logging.getLogger("qa.create")

@step(u'a configured python environment')
def configured_python_environment(context):
    #__logger__.info(" >> Environment: '%s'", context.config.userdata['environment'])
    __logger__.info(" >> Environment: '%s'", context.config.userdata)
    __logger__.info(" >> Dict value in 'Given' step: '%s'", context.dict)


@step(u'I create a new dict with key with this values')
def create_new_dict(context):
    for row in context.table:
        context.dict.update({row["key"]: row["value"]})
    __logger__.info(" >> Dict value in 'Then' step (after execution): '%s'", context.dict)


@step(u'the dict is created')
def the_dict_is_created(context):
    assert_that(isinstance(context.dict, dict), is_(True),
                "The dict has not been created")


@step(u'the key "(?P<key>.*)" has the value "(?P<value>.*)"')
def the_length_is(context, key, value):
    assert_that(key, is_in(context.dict),
                "The is not in the dict")
    assert_that(context.dict[key], is_(equal_to(value)),
                "The value is not the expected")


# @given(u'a configured python environment')
# @step(u'a configured python environment')
#def configured_python_environment(context):
 #   assert_that(context.list, is_(None),
  #              "The list is not defined in Behave context")


# @when(u'I create a new empty list')
@step(u'I create a new empty list')
def create_an_empty_list(context):
    context.list = list()


# @when(u'I create a new list with values "(?P<values>.*)"')
@step(u'I create a new list with values "(?P<values>.*)"')
def create_new_list_with_values(context, values):
    array_values = values.split(",")
    context.list = list(array_values)


# @then(u'the list is created')
@step(u'the list is created')
def the_list_is_created(context):
    assert_that(isinstance(context.list, list), is_(True),
                "The list has not been created")


# @then(u'the length of the list is "(?P<length>\d*)"')
@step(u'the length of the list is "(?P<length>\d*)"')
def the_length_is(context, length):
    assert_that(len(context.list), is_(equal_to(int(length))),
                "The length is not the expected one")


# @then(u'the list has got next content')
@step(u'the list has got next content')
def the_list_has_got_content(context):
    for row in context.table:
        assert_that(context.list[int(row['position'])], is_(equal_to(row['content'])),
                    "The content is not the expected one")


# @given(u'a created empty list')
@step(u'a created empty list')
def a_created_list(context):
    context.execute_steps(u'''
         Given  a configured python environment
         When   I create a new empty list
         Then   the list is created
         And    the length of the list is "0"
    ''')
