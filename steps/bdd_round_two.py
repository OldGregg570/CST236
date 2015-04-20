from behave import given, when, then
from source.System import SpeedBenchmarkSystem as System
from source.System import City

"""
When entering the driving speed I would like to be able to specify
some preset values (Porsche, Bus, Cement Truck, laden swallow)
"""
@given('I know some relative speed')
def step_impl(context):
    context.speed = 'laden swallow'
    context.sys = System()
    pass

@when('I input the driving speed')
def step_impl(context):
    context.sys.set_speed_estimate(200)
    pass

@then('I can specify a relative speed')
def step_impl(context):
    context.sys.set_speed_estimate(200, context.speed)
    pass

"""
When selecting a city I want to be able to create a new city so I have more options
"""
@given('I am selecting a city')
def step_impl(context):
    ## Don't know what this means...
    context.sys = System('./test_data')
    pass

@when('I want to create a new city')
def step_impl(context):
    context.sys.add_city(City('test', 200, 200))
    pass

@then('I am able to create a new city')
def step_impl(context):
    # ??
    pass


"""
When I enter a new city, I want the results to be written to the city file.

TODO: Find out about redundant 'given' / 'when'
"""
@given('I have input a new city')
def step_impl(context):
    context.sys = System('./test_data')
    pass

@when('I input the city')
def step_impl(context):
    context.sys.add_city(City('test', 200, 200))
    pass

@then('the new city is saved to the file')
def step_impl(context):
    pass
