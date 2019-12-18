# Created by ********  chomri01 at 12/18/2019

# Feature Name :: --

# To Do ::-
import sys
from selenium import webdriver
from TestAutomation.utils.constaints_locator_details import solution_location
chrome_path='D:\Learning\PythonworkStation\AutomationTesting\software\chromedriver.exe'
firefox_path='D:\TestAutomation\TestResults\geckodriver-v0.26.0-win64\geckodriver.exe'


def start_chrome_driver():
	try:
		chrome_options=webdriver.ChromeOptions()
		chrome_options.add_argument('--disable-extensions')
		chrome_options.add_argument('--headless')
		prefs = {"download.default_directory": solution_location+"//testdata"}
		chrome_options.add_experimental_option("prefs", prefs)
		driver=webdriver.Chrome(options=chrome_options,executable_path=chrome_path)
		return driver
	except Exception as ex:
		print(sys.exc_info())
		return None


def start_firefox_driver():
	try:
		firefox_option=webdriver.FirefoxOptions()
		firefox_option.add_argument('--disable-extensions')
		firefox_option.add_argument('--headless')
		firefox_profile=webdriver.FirefoxProfile()
		firefox_profile.set_preference("browser.download.folderList", 2)
		firefox_profile.set_preference("browser.download.manager.showWhenStarting", False)
		firefox_profile.set_preference("browser.download.dir", solution_location+"//testdata")
		firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
		driver=webdriver.Firefox(firefox_profile=firefox_profile,firefox_options=firefox_option,executable_path=firefox_path)
		return driver
	except Exception as s:
		print(sys.exc_info())
		return None
