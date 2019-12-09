# Created by ********  chomri01 at 12/9/2019

# Feature Name :: --

# To Do ::-
from TestAutomation.utils.logger_report_details import *

def before_feature(context, scenario):
	start_logger()
	logging.info("Feature Name is ----" + str(scenario.name))
	pass


def before_scenario(context, scenario):
	logging.info("This is before scenario ")
