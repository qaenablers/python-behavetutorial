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
#after_all

# Runner Operation: Scenarios Outlines
# ===========================================
#before_all
#for feature in all_features:
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
#after_all

import logging
from behave.log_capture import capture

logging.basicConfig(filename="qa.log", level=logging.DEBUG)
__logger__ = logging.getLogger("qa")


#@capture
def before_feature(context, feature):
    __logger__.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    __logger__.info("BEFORE FEATURE")


#@capture
def after_feature(context, feature):
    __logger__.info("AFTER FEATURE")
    __logger__.info("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


def before_scenario(context, scenario):
    __logger__.info("==>>")
    __logger__.info("BEFORE SCENARIO")
    context.dict = dict()


def after_scenario(context, scenario):
    __logger__.info("AFTER SCENARIO")
    __logger__.info("<<==")


def before_step(context, step):
    __logger__.info("BEFORE STEP")


def after_step(context, step):
    __logger__.info("AFTER STEP")
