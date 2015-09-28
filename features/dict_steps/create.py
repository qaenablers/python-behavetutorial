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
    __logger__.info(" >> Environment: '%s'", context.config.userdata['environment'])
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
