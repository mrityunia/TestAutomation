# Created by ********  chomri01 at 12/18/2019

# Feature Name :: --

# To Do ::-

from TestAutomation.pages.base_page_details import *
from TestAutomation.utils.constaints_locator_details import *
import logging


class GAM_Home(BasePage):
	def __init__(self, context):
		BasePage.__init__(
			self,
			context.Browser
		)

	def open_GAM_home_page(self):
		try:

			self.Browser.maximize_window()
			logging.info("Browser is maximize ")
			self.Browser.get(gam_url)
			logging.info("URL is " + str(gam_url))
			return True
		except Exception:
			return False
	def Get_GAM_page_title(self):
		page_title = self.Browser.title
		logging.info("Page title is "+str(page_title))
		return page_title
	def get_GAM_page_source(self):
		page_source = self.Browser.page_source
		logging.info("Page source is "+str(page_source)[:20])
		return page_source
