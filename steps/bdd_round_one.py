from behave import given, when, then
from source.System import SpeedBenchmarkSystem as System
"""
When researching speeds I want the cities, distances and connection speeds
to be read in from a file so I don't have to type them all in
"""

@given('A file is provided')
def step_impl(context):
    context.filepath='./test_data'

@when('the system is initialized')
def step_impl(context):
    context.sys = System(context.filepath)

@then('The system reads the cities, distances and connection speeds from file')
def step_impl(context):
    assert context.sys.cities[0].city == 'Portland'


"""
When researching speeds I want to be able to select an estimated speed so
I can see whether the network or driving would be faster
"""

@given('I want to know which route would be faster')
def step_impl(context):
    context.sys = System()

@when('I select a speed estimate')
def step_impl(context):
    context.sys.set_speed_estimate(200)

@then('the system will indicate whether the network or driving would be faster')
def step_impl(context):
    assert context.sys.network_is_faster()


"""
When researching speeds I want to be able to select a hard drive size (in GB)
so I can have more data
"""

@given('I know my HD size')
def step_impl(context):
    context.hd_size = 10000

@when('I select HD Size')
def step_impl(context):
    context.sys = System(None, [], context.hd_size)

@then('the system will allocate more space so I can have more data')
def step_impl(context):
    assert context.sys.hd_size == 10000



"""
When I enter a city, a speed and hard drive size I want to see whether the network
or the hard drive would be faster
"""

@given('I know the city, speed, and HD size')
def step_impl(context):
    context.city = 'Portland'
    context.speed = 1000
    context.hd_size = 2000
    pass

@when('I input the city, speed, and HD size')
def step_impl(context):
    context.sys = System('./test_data', [], context.hd_size)

@then('the system will determine and indicate which would be better')
def step_impl(context):
    assert context.sys.get_best_path(context.city, context.speed, context.hd_size)

@then('the system can log the difference in times between the network and the HD')
def step_impl(context):
    assert context.sys.get_speed_diff(context.city, context.speed, context.hd_size) == 1000




