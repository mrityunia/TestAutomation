# Created by ********  chomri01 at 12/9/2019

# Feature Name :: --

# To Do ::-

from behave import given, then, when
from TestAutomation.pages.home_page_details import *


@given(u'the user has navigated to the page "GAM dashboard"')
def step_impl(context):
	global gam_home
	gam_home = GAM_Home(context=context)
	assert gam_home.open_GAM_home_page()==True, "GAM home page  is not opened"


@then(u'the user sees the page url contains "{titlematch}"')
def step_impl(context,titlematch):
	assert str(gam_home.Get_GAM_page_title()).__contains__(titlematch)==True,"Page title is invalid"

@then(u'the user sees the "{pagesource}" in the PageSource')
def step_impl(context,pagesource):
	assert str(gam_home.get_GAM_page_source()).__contains__(pagesource)==True,"page source is invalid"



@given(u'the user has captured the now showing xxxx items number on the GAM home screen')
def step_impl(context):
	pass


@when(u'the user has exports the CSV file from GAM')
def step_impl(context):
	pass

@then(u'the user sees that the number of rows in the CSV is equal to the "Now showing xxxx items" plus one')
def step_impl(context):
	pass

@then(u'the user deletes the CSV file')
def step_impl(context):
	pass