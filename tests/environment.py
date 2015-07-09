# -*- coding: utf-8 -*-

# Runner Operation: Scenarios
# ===========================================
# before_all
# for feature in all_features:
#    before_feature
#    for scenario in feature.scenarios:
#        before_scenario
#        for step in scenario.steps:
#            before_step
#                step.run()
#            after_step
#        after_scenario
#    after_feature
# after_all

# Runner Operation: Scenarios Outlines
# ===========================================
# before_all
# for feature in all_features:
#    before_feature
#    for outline in feature.scenarios:
#        for scenario in outline.scenarios:
#            before_scenario
#            for step in scenario.steps:
#                before_step
#                    step.run()
#                after_step
#            after_scenario
#    after_feature
# after_all

import logging
from behave.log_capture import capture
from behave import model

logging.basicConfig(filename="qa.log", level=logging.DEBUG)
__logger__ = logging.getLogger("qa")


# @capture
# def before_feature(context, feature):
#    __logger__.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#    __logger__.info("BEFORE FEATURE")
#    __logger__.info(feature)
#    __logger__.info(context)

def before_feature(context, feature):
    # model.init(environment='test')
    __logger__.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    __logger__.info("NORMAL BEFORE FEATURE")
    __logger__.info('Feature Name: {}'.format(feature))
    __logger__.info('Context includes {}'.format(context))
    if 'specialtag' in context.tags:
        __logger__.info("***********SPECIAL TAG BEFORE FEATURE --->>>>>>>>")

def before_scenario(context, scenario):
    __logger__.info("==>>")
    __logger__.info("BEFORE SCENARIO")
    context.dict = dict()


def before_step(context, step):
    __logger__.info("BEFORE STEP")
    __logger__.info(step)
    __logger__.info(context)


# @capture
def after_feature(context, feature):
    __logger__.info("AFTER FEATURE")
    __logger__.info("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    if 'specialtag' in context.tags:
        __logger__.info("**********_SPECIAL TAG AFTER FEATURE ")

def after_scenario(context, scenario):
    __logger__.info("AFTER SCENARIO")
    __logger__.info("<<==")


def after_step(context, step):
    __logger__.info("AFTER STEP")
    if 'specialtag' in context.tags:
        __logger__.info("**********_SPECIAL TAG AFTER STEP ")
