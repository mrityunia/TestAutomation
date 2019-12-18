# Created by ********  chomri01 at 12/9/2019

# Feature Name :: --

# To Do ::-
from TestAutomation.utils.constaints_locator_details import browsers_name
from TestAutomation.utils.logger_report_details import *
from TestAutomation.utils import driver_details
import logging
def before_feature(context, scenario):
	start_logger()
	logging.info("Feature Name is ----" + str(scenario.name))
	pass

def before_scenario(context, scenario):
	logging.info("This is before scenario ")
	global browsers
	for tag in scenario.tags:
		if tag in browsers_name:
			logging.info(str(tag)+" Browser starting....")
			browsers=tag
			break
		else:
			logging.info("Chrome Default Browser starting.....")
			browsers='Chrome'
			pass
	if str(browsers).lower() =='chrome':
		context.Browser=driver_details.start_chrome_driver()
	elif str(browsers).lower() == 'firefox':
		context.Browser = driver_details.start_firefox_driver()
