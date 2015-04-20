from behave import given, when, then

"""
When researching speed I want to be able to create a route of 1 - 10 cities so I can get a more accurate picture
"""
@given('I am researching speed')
def step_impl(context):
    pass

@when('I create a list of cities')
def step_impl(context):
    pass

@then('I can get a more accurate picture')
def step_impl(context):
    pass


"""
When I start the application I want to enter my starting city, so I know where I am
"""
@given('the application has been started')
def step_impl(context):
    pass

@when('I enter my start city')
def step_impl(context):
    pass

@then('the application knows where I am')
def step_impl(context):
    pass

"""
When researching speeds I want to be able to account for network latency so that my numbers are more accurate.
"""
@given('there is network latency')
def step_impl(context):
    pass

@when('I research speeds')
def step_impl(context):
    pass

@then('network lag is accounted for')
def step_impl(context):
    pass


"""
When selecting a hard drive I want to enter the hard drive speed (gb/s) to account for the time to copy.
"""
@given('I know my HD speed')
def step_impl(context):
    pass

@when('I input the speed')
def step_impl(context):
    pass

@then('the latency is accounted for')
def step_impl(context):
    pass