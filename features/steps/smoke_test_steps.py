# Created by ********  chomri01 at 12/9/2019

# Feature Name :: --

# To Do ::-

from behave import given,then,when
import logging
@given(u'The user opens application')
def step_impl(context):
	logging.info(u'STEP: Given The user opens application')


@then(u'application is opened')
def step_impl(context):
	logging.info(u'STEP: Then application is opened')


@given(u'the user clicks on sign in')
def step_impl(context):
	logging.info(u'STEP: Given the user clicks on sign in')


@when(u'the user enters user id and password')
def step_impl(context):
	logging.info(u'STEP: When the user enters user id and password')


@when(u'clicks on SignIn')
def step_impl(context):
	logging.info(u'STEP: When clicks on SignIn')


@then(u'the user is getting success message')
def step_impl(context):
	logging.info(u'STEP: Then the user is getting success message')
