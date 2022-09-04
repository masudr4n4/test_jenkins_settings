from behave import *
import random



@given("I am on the homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I mark the test as passed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("how are u:?")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given how are u:?')


@given("how are u?")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given how are u?')



@given("you are on the new page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert 1 == random.randint(1,2)