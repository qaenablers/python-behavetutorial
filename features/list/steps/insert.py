# -*- coding: utf-8 -*-

import behave
from behave import step
import logging

behave.use_step_matcher("re")
__logger__ = logging.getLogger('qa.insert')

@step(u'I add the value "(?P<value>.*)" at the end of the list')
def add_value_at_the_end(context, value):
    #print "Creating new list"
    __logger__.info("Append new value %s", value)
    context.list.append(value)


@step(u'I add the value "(?P<value>.*)" at the beginning of the list')
def add_value_at_the_beginning(context, value):

    # This code is to fail the @test6
    value = value.replace("qa", "QA")
    __logger__.debug("List data: '%s'", value)  # --logging-level DEBUG
    __logger__.info("Value to check if is on list: '%s'", value)

    context.list.insert(0, value)
