# Created by ********  chomri01 at 8/13/2019

# Feature Name :: --

# To Do ::-

from behave.__main__ import main as behave_main
from sys import exit

if __name__ == '__main__':
   # exit(behave_main('Jira/features/SmokeTest.feature --tags=@debug --no-capture'))
    exit(behave_main('features/smoke_test.feature --no-capture'))
