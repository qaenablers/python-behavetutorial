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


def before_all(context):
    __logger__.info("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
    __logger__.info("¡¡    Hooks for 'LIST' steps    !!")
    __logger__.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def before_scenario(context, scenario):
    context.list = None