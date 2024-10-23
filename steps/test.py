from behave import *
from dask.bag import assert_eq

from Cities import game
from unittest.mock import patch
from io import StringIO

@given('Computer start game')
def step_game(context):
    context._inst = game()
    context.g_inst.first()

@then('Computer make a move')
def step_out(context):
    context.assertEqual( context.g_inst.pcs_move(), None)

@then('Computer done')
def step_out(context):
    context.assertEqual( context.g_inst.pcs_move(), None)

@when('I am make a move')
def step_input(context):
    context.myIn = \
        context.g_inst.cdb_getter()[
            context.g_inst.cdb_getter()['city_ascii'].str[0] ==  context.g_inst.pc_getter()[-1].upper()].sample().values[
            0, 1]
    with patch('builtins.input', return_value=myIn):
        assert_eq( context.g_inst.players_move(), None)

@when('I'm done')